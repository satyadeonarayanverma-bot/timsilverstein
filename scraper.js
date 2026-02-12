const axios = require('axios');
const cheerio = require('cheerio');
const fs = require('fs-extra');
const path = require('path');
const url = require('url');
const crypto = require('crypto');

const BASE_URL = 'https://altcloudai.com';
const OUTPUT_DIR = path.join(__dirname);
const ASSETS_DIR = path.join(OUTPUT_DIR, 'assets');

// Configuration
const CONCURRENT_LIMIT = 5;
const USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36';

// State
const visitedUrls = new Set();
const downloadedAssets = new Map(); // url -> localFilename

async function downloadAsset(assetUrl, referer) {
    if (!assetUrl) return null;

    // Clean URL
    assetUrl = assetUrl.trim();
    if (assetUrl.startsWith('data:')) return null; // Skip data URIs

    // Resolve URL absolute
    const absoluteUrl = url.resolve(BASE_URL, assetUrl);

    // Check cache
    if (downloadedAssets.has(absoluteUrl)) {
        return downloadedAssets.get(absoluteUrl);
    }

    const localFilename = getLocalFilename(absoluteUrl);
    const localPath = path.join(ASSETS_DIR, localFilename);
    const relativePath = `assets/${localFilename}`;

    downloadedAssets.set(absoluteUrl, relativePath); // Mark as in-progress/done

    try {
        const response = await axios({
            method: 'GET',
            url: absoluteUrl,
            responseType: 'arraybuffer', // Better for binary + text
            headers: {
                'User-Agent': USER_AGENT,
                'Referer': referer || BASE_URL
            },
            validateStatus: (status) => status < 500, // Accept 404s to avoid throwing
            timeout: 15000
        });

        if (response.status !== 200) {
            console.warn(`[${response.status}] Failed to download: ${absoluteUrl}`);
            return relativePath; // Return the path anyway so the link exists
        }

        let content = response.data;

        // If it's a CSS file, we must parse it for recursively finding assets
        if (absoluteUrl.endsWith('.css') || response.headers['content-type']?.includes('css')) {
            const cssContent = content.toString('utf8');
            const { newCss } = await processCss(cssContent, absoluteUrl);
            content = Buffer.from(newCss, 'utf8');
        }

        await fs.outputFile(localPath, content);
        return relativePath;

    } catch (error) {
        console.error(`Error downloading ${absoluteUrl}: ${error.message}`);
        return relativePath; // Return path to minimize broken layout impact
    }
}

async function processCss(cssContent, cssUrl) {
    const assetsToDownload = [];
    const newCss = cssContent.replace(/url\s*\((['"]?)(.*?)\1\)/gi, (match, quote, urlInside) => {
        if (!urlInside || urlInside.startsWith('data:')) return match;

        // Resolve recursive assets relative to the CSS file location
        const absoluteAssetUrl = url.resolve(cssUrl, urlInside);
        const localFilename = getLocalFilename(absoluteAssetUrl);

        // Queue download in background
        assetsToDownload.push(downloadAsset(absoluteAssetUrl, cssUrl));

        return `url('${localFilename}')`; // Flattened structure
    });

    Promise.all(assetsToDownload).catch(e => console.error("CSS Asset error", e));
    return { newCss };
}

function getLocalFilename(fileUrl) {
    const parsed = url.parse(fileUrl);
    let basename = path.basename(parsed.pathname || 'index.html');

    // Fix extension key issues (e.g. image.jpg?v=1)
    if (!path.extname(basename) || basename.length > 50) {
        // Try to guess from path or default to .html / .asset
        if (fileUrl.includes('.css')) basename += '.css';
        else if (fileUrl.includes('.js')) basename += '.js';
        else if (fileUrl.includes('.png')) basename += '.png';
        else if (fileUrl.includes('.jpg')) basename += '.jpg';
        else if (!path.extname(basename)) basename += '.html';
    }

    const safeName = basename.replace(/[^a-zA-Z0-9.-]/g, '_');
    const hash = crypto.createHash('md5').update(fileUrl).digest('hex').substring(0, 8);
    return `${hash}_${safeName}`;
}

async function processPage(pageUrl) {
    const parsedUrl = url.parse(pageUrl);
    let filename = 'index.html';

    if (parsedUrl.pathname && parsedUrl.pathname !== '/') {
        filename = parsedUrl.pathname.replace(/^\/|\/$/g, '').replace(/\//g, '-') + '.html';
    }

    if (visitedUrls.has(pageUrl)) return;
    visitedUrls.add(pageUrl);

    console.log(`Scraping Page (v4): ${pageUrl} -> ${filename}`);

    try {
        const response = await axios.get(pageUrl, {
            headers: { 'User-Agent': USER_AGENT }
        });
        const $ = cheerio.load(response.data);
        const promises = [];

        // Helper
        const queueAsset = (url, context) => {
            if (!url) return Promise.resolve(null);
            return downloadAsset(url, pageUrl);
        };

        // 1. Standard Assets (Link, Script, Img, Iframe)
        $('link[href]').each((i, e) => promises.push(queueAsset($(e).attr('href')).then(p => p && $(e).attr('href', p))));
        $('script[src]').each((i, e) => promises.push(queueAsset($(e).attr('src')).then(p => p && $(e).attr('src', p))));
        $('iframe[src]').each((i, e) => promises.push(queueAsset($(e).attr('src')).then(p => p && $(e).attr('src', p))));

        $('img').each((i, e) => {
            const src = $(e).attr('src');
            const dataSrc = $(e).attr('data-src');
            const dataLazy = $(e).attr('data-lazy-src');

            // Prioritize data-src/lazy for high res
            const targetSrc = dataSrc || dataLazy || src;

            if (targetSrc) {
                promises.push(queueAsset(targetSrc).then(p => {
                    if (p) {
                        $(e).attr('src', p);
                        $(e).removeAttr('data-src');
                        $(e).removeAttr('data-lazy-src');
                        $(e).removeAttr('srcset'); // Kill srcset to force our local src
                    }
                }));
            }
        });

        // 2. Inline Styles & Backgrounds
        $('*[style]').each((i, e) => {
            const style = $(e).attr('style');
            if (style && style.includes('url(')) {
                const matches = style.matchAll(/url\(['"]?(.*?)['"]?\)/g);
                for (const match of matches) {
                    if (match[1]) {
                        promises.push(queueAsset(match[1]).then(p => {
                            if (p) {
                                const newStyle = $(e).attr('style').replace(match[1], p);
                                $(e).attr('style', newStyle);
                            }
                        }));
                    }
                }
            }
        });

        // 3. ELEMENTOR SPECIFIC: data-settings JSON
        $('*[data-settings]').each((i, e) => {
            try {
                const settingsJson = $(e).attr('data-settings');
                const settings = JSON.parse(settingsJson);

                // Check for background_image
                if (settings.background_image && settings.background_image.url) {
                    const oldUrl = settings.background_image.url;
                    promises.push(queueAsset(oldUrl).then(p => {
                        if (p) {
                            settings.background_image.url = p;
                            $(e).attr('data-settings', JSON.stringify(settings));
                        }
                    }));
                }
            } catch (err) {
                // Ignore parse errors
            }
        });

        // 4. CRAWL: Internal Links
        const linksToVisit = [];
        $('a[href]').each((i, e) => {
            let href = $(e).attr('href');
            if (!href || href.startsWith('#') || href.startsWith('mailto:') || href.startsWith('tel:') || href.startsWith('javascript:')) return;

            const absoluteHref = url.resolve(BASE_URL, href);
            const parsedHref = url.parse(absoluteHref);

            // Internal only
            if (parsedHref.hostname === 'altcloudai.com' || parsedHref.hostname === 'www.altcloudai.com') {
                let linkFilename = 'index.html';
                if (parsedHref.pathname && parsedHref.pathname !== '/') {
                    linkFilename = parsedHref.pathname.replace(/^\/|\/$/g, '').replace(/\//g, '-') + '.html';
                }

                // FIX: Preserve Hash/Fragment
                if (parsedHref.hash) {
                    linkFilename += parsedHref.hash;
                }

                $(e).attr('href', linkFilename);

                const normalizedUrl = `${parsedHref.protocol}//${parsedHref.hostname}${parsedHref.pathname}`;
                if (!visitedUrls.has(normalizedUrl)) {
                    linksToVisit.push(normalizedUrl);
                }
            }
        });

        await Promise.all(promises);

        const outputPath = path.join(OUTPUT_DIR, filename);
        await fs.outputFile(outputPath, $.html());

        for (const nextUrl of linksToVisit) {
            await processPage(nextUrl);
        }

    } catch (error) {
        console.error(`Failed to process page ${pageUrl}: ${error.message}`);
    }
}

async function main() {
    await fs.ensureDir(ASSETS_DIR);
    console.log("Starting Deep Clone V4 (Link Fix)...");
    await processPage(BASE_URL + '/');
    console.log("Deep Clone V4 Complete!");
}

main();
