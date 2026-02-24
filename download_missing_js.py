import os
import requests
import re
from urllib.parse import urlparse, unquote

base_dir = r"c:\Users\ADITYA VERMA\OneDrive\Documents\New folder (20)\altcloudaiclone"
assets_dir = os.path.join(base_dir, "assets")
os.makedirs(assets_dir, exist_ok=True)

# The list of missing files reported by fix_js_paths.py (we strip the cache hash prefix)
missing_files = [
    "61a6fa59_jquery-migrate.min.js",
    "ff01a0c1_jquery.blockUI.min.js",
    "7870de42_add-to-cart.min.js",
    "a925157d_hooks.min.js",
    "6078b9bb_frontend-modules.min.js",
    "e80a2958_core.min.js",
    "cb1a3749_hc-offcanvas-nav.min.js",
    "f7ac5205_order-attribution.min.js",
    "485d7491_frontend.js"
]

# We extract the base filename
core_filenames = [f.split('_', 1)[1] if '_' in f else f for f in missing_files]

# We need to find the actual live URLs for these from the original website. 
# Since we might not know the exact path on the server, we can parse original_index.html (the raw scrape)
original_html_path = os.path.join(base_dir, "original_index.html")
live_urls = []

if os.path.exists(original_html_path):
    with open(original_html_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    for core_name in core_filenames:
        # Search for src=".../core_name"
        pattern = r'src="([^"]*' + re.escape(core_name) + r'[^"]*)"'
        matches = re.findall(pattern, content)
        if matches:
            live_urls.append(matches[0])
        else:
            print(f"Could not find original live URL for {core_name}")

print(f"Found {len(live_urls)} live URLs to download.")

for url in live_urls:
    try:
        print(f"Downloading {url}...")
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200:
            # We want to save it as the EXACT hashed name that index.html currently expects, OR just download it and let fix_js_paths run again.
            # It's safer to download it as the core name, and then run fix_js_paths.py
            
            # Extract filename from URL
            parsed_url = urlparse(url)
            filename = os.path.basename(unquote(parsed_url.path))
            
            # Remove any query params like ?ver=6.4.3
            if '?' in filename:
                filename = filename.split('?')[0]
                
            local_path = os.path.join(assets_dir, filename)
            with open(local_path, 'wb') as f:
                f.write(response.content)
            print(f"Saved to {filename}")
        else:
            print(f"Failed to download {url} - Status: {response.status_code}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")
