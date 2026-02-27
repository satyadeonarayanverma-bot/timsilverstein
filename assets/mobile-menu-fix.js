/**
 * Mobile Menu Fix v5 – Direct Injection Approach
 * ------------------------------------------------
 * Problem:  Elementor's responsive CSS hides the navigation-menu widget
 *           (.elementor-widget-navigation-menu) via display:none on mobile,
 *           which also hides the built-in .hfe-nav-menu__toggle.
 *
 * Solution: Inject a NEW hamburger button directly into the header bar
 *           (.e-con-inner) as a sibling of the logo widget.  Build a
 *           fullscreen overlay menu from the existing nav links.
 */
(function () {
    'use strict';

    /* ─────────────────────── CSS ─────────────────────── */
    var css = [
        '@media only screen and (max-width: 767px) {',

        /* Header bar layout: logo left, hamburger right */
        '  .elementor-element-3550465 > .e-con-inner {',
        '    display: flex !important;',
        '    flex-direction: row !important;',
        '    flex-wrap: nowrap !important;',
        '    align-items: center !important;',
        '    justify-content: space-between !important;',
        '    width: 100% !important;',
        '    padding-right: 12px !important;',
        '  }',

        /* Logo sizing */
        '  .elementor-element-3550465 .elementor-widget-site-logo {',
        '    flex: 0 1 auto !important;',
        '    max-width: 65% !important;',
        '  }',

        /* HIDE the original nav widget entirely (it is display:none anyway) */
        '  .elementor-element-3550465 .elementor-widget-navigation-menu {',
        '    display: none !important;',
        '  }',

        /* ── Injected Hamburger Button ── */
        '  #injected-hamburger {',
        '    display: flex !important;',
        '    align-items: center;',
        '    justify-content: center;',
        '    cursor: pointer;',
        '    padding: 8px;',
        '    z-index: 10001;',
        '    flex-shrink: 0;',
        '    background: none;',
        '    border: none;',
        '    -webkit-tap-highlight-color: transparent;',
        '  }',
        '  #injected-hamburger svg {',
        '    width: 28px;',
        '    height: 28px;',
        '    fill: #ffffff;',
        '    display: block;',
        '  }',

        /* ── Fullscreen Overlay ── */
        '  #mobile-nav-overlay {',
        '    position: fixed;',
        '    top: 0; left: 0; right: 0; bottom: 0;',
        '    width: 100vw; height: 100vh;',
        '    background: rgba(10, 10, 10, 0.97);',
        '    z-index: 99999;',
        '    display: none;',
        '    flex-direction: column;',
        '    overflow-y: auto;',
        '    -webkit-overflow-scrolling: touch;',
        '    padding: 70px 0 30px;',
        '    animation: mobileOverlayFade 0.25s ease-out;',
        '  }',
        '  #mobile-nav-overlay.open {',
        '    display: flex !important;',
        '  }',
        '  @keyframes mobileOverlayFade {',
        '    from { opacity: 0; transform: translateY(-8px); }',
        '    to   { opacity: 1; transform: translateY(0);    }',
        '  }',

        /* Close button */
        '  #mobile-nav-close {',
        '    position: fixed;',
        '    top: 16px; right: 16px;',
        '    z-index: 100000;',
        '    width: 40px; height: 40px;',
        '    display: flex;',
        '    align-items: center;',
        '    justify-content: center;',
        '    cursor: pointer;',
        '    background: rgba(255,255,255,0.1);',
        '    border: none;',
        '    border-radius: 8px;',
        '    -webkit-tap-highlight-color: transparent;',
        '  }',
        '  #mobile-nav-close svg {',
        '    width: 20px; height: 20px;',
        '    fill: #ffffff;',
        '  }',

        /* Branding inside overlay */
        '  #mobile-nav-brand {',
        '    padding: 0 24px 12px;',
        '    border-bottom: 1px solid rgba(255,255,255,0.1);',
        '    margin-bottom: 8px;',
        '  }',
        '  #mobile-nav-brand .brand-main {',
        '    font-family: Arial, sans-serif;',
        '    font-size: 22px;',
        '    font-weight: 800;',
        '    color: #ffffff;',
        '  }',
        '  #mobile-nav-brand .brand-accent {',
        '    font-family: Arial, sans-serif;',
        '    font-size: 22px;',
        '    font-weight: 400;',
        '    color: #33a1fd;',
        '    margin-left: 5px;',
        '  }',

        /* Menu list */
        '  #mobile-nav-overlay .mobile-nav-list {',
        '    list-style: none;',
        '    margin: 0; padding: 0;',
        '    width: 100%;',
        '  }',
        '  #mobile-nav-overlay .mobile-nav-item {',
        '    border-bottom: 1px solid rgba(255,255,255,0.08);',
        '  }',
        '  #mobile-nav-overlay .mobile-nav-item:last-child {',
        '    border-bottom: none;',
        '  }',
        '  #mobile-nav-overlay .mobile-nav-link {',
        '    display: flex;',
        '    justify-content: space-between;',
        '    align-items: center;',
        '    padding: 16px 24px;',
        '    color: #ffffff;',
        '    text-decoration: none;',
        '    font-size: 16px;',
        '    font-family: inherit;',
        '  }',
        '  #mobile-nav-overlay .mobile-nav-link:hover,',
        '  #mobile-nav-overlay .mobile-nav-link:active {',
        '    background: rgba(255,255,255,0.06);',
        '  }',

        /* Sub-menu toggle arrow */
        '  #mobile-nav-overlay .mobile-sub-toggle {',
        '    display: inline-flex;',
        '    align-items: center;',
        '    justify-content: center;',
        '    padding: 8px 12px;',
        '    cursor: pointer;',
        '    color: #888;',
        '    font-size: 16px;',
        '    transition: transform 0.2s ease;',
        '    -webkit-tap-highlight-color: transparent;',
        '    border: none;',
        '    background: none;',
        '  }',
        '  #mobile-nav-overlay .mobile-sub-toggle.rotated {',
        '    transform: rotate(180deg);',
        '  }',

        /* Sub-menu */
        '  #mobile-nav-overlay .mobile-sub-menu {',
        '    list-style: none;',
        '    margin: 0; padding: 0;',
        '    display: none;',
        '    background: rgba(255,255,255,0.03);',
        '  }',
        '  #mobile-nav-overlay .mobile-sub-menu.open {',
        '    display: block;',
        '  }',
        '  #mobile-nav-overlay .mobile-sub-menu .mobile-nav-link {',
        '    padding: 14px 24px 14px 40px;',
        '    color: #b0b0b0;',
        '    font-size: 15px;',
        '  }',
        '  #mobile-nav-overlay .mobile-sub-menu .mobile-nav-link:hover {',
        '    color: #ffffff;',
        '    background: rgba(255,255,255,0.04);',
        '  }',

        '}', /* end mobile media query */

        /* Desktop: hide injected elements */
        '@media only screen and (min-width: 768px) {',
        '  #injected-hamburger,',
        '  #mobile-nav-overlay,',
        '  #mobile-nav-close {',
        '    display: none !important;',
        '  }',
        '}'
    ].join('\n');

    var styleEl = document.createElement('style');
    styleEl.id = 'mobile-menu-fix-styles';
    styleEl.textContent = css;
    document.head.appendChild(styleEl);


    /* ─────────────────────── JS ─────────────────────── */
    function init() {
        /* Find the header bar's inner container */
        var headerEl = document.querySelector('.elementor-element-3550465');
        if (!headerEl) return;
        var conInner = headerEl.querySelector('.e-con-inner');
        if (!conInner) return;

        /* Prevent double-init */
        if (document.getElementById('injected-hamburger')) return;

        /* ── 1. Create the hamburger button ── */
        var hamburgerBtn = document.createElement('button');
        hamburgerBtn.id = 'injected-hamburger';
        hamburgerBtn.setAttribute('aria-label', 'Open menu');
        hamburgerBtn.innerHTML =
            '<svg viewBox="0 0 448 512" xmlns="http://www.w3.org/2000/svg">' +
            '<path d="M432 416H16a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h416a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm0-128H16a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h416a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm0-128H16a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h416a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm0-128H16A16 16 0 0 0 0 48v32a16 16 0 0 0 16 16h416a16 16 0 0 0 16-16V48a16 16 0 0 0-16-16z"></path>' +
            '</svg>';
        conInner.appendChild(hamburgerBtn);

        /* ── 2. Build the fullscreen overlay ── */
        var overlay = document.createElement('div');
        overlay.id = 'mobile-nav-overlay';

        /* Close button */
        var closeBtn = document.createElement('button');
        closeBtn.id = 'mobile-nav-close';
        closeBtn.setAttribute('aria-label', 'Close menu');
        closeBtn.innerHTML =
            '<svg viewBox="0 0 352 512" xmlns="http://www.w3.org/2000/svg">' +
            '<path d="M242.72 256l100.07-100.07c12.28-12.28 12.28-32.19 0-44.48l-22.24-22.24c-12.28-12.28-32.19-12.28-44.48 0L176 189.28 75.93 89.21c-12.28-12.28-32.19-12.28-44.48 0L9.21 111.45c-12.28 12.28-12.28 32.19 0 44.48L109.28 256 9.21 356.07c-12.28 12.28-12.28 32.19 0 44.48l22.24 22.24c12.28 12.28 32.19 12.28 44.48 0L176 322.72l100.07 100.07c12.28 12.28 32.19 12.28 44.48 0l22.24-22.24c12.28-12.28 12.28-32.19 0-44.48L242.72 256z"></path>' +
            '</svg>';
        overlay.appendChild(closeBtn);

        /* Branding at top of overlay */
        var brand = document.createElement('div');
        brand.id = 'mobile-nav-brand';
        brand.innerHTML = '<span class="brand-main">Cloudiva</span><span class="brand-accent">.ai</span>';
        overlay.appendChild(brand);

        /* Build menu items from existing nav */
        var navList = document.createElement('ul');
        navList.className = 'mobile-nav-list';

        var existingItems = headerEl.querySelectorAll('nav ul.hfe-nav-menu > li');
        existingItems.forEach(function (li) {
            var newItem = document.createElement('li');
            newItem.className = 'mobile-nav-item';

            /* Main link */
            var originalLink = li.querySelector(':scope > a.hfe-menu-item, :scope > .hfe-has-submenu-container a.hfe-menu-item');
            if (originalLink) {
                var link = document.createElement('a');
                link.className = 'mobile-nav-link';
                link.href = originalLink.href;
                link.textContent = originalLink.textContent.trim();

                /* Has sub-menu? */
                var originalSub = li.querySelector(':scope > ul.sub-menu');
                if (originalSub) {
                    var toggle = document.createElement('button');
                    toggle.className = 'mobile-sub-toggle';
                    toggle.textContent = '▾';
                    toggle.setAttribute('aria-label', 'Expand sub-menu');

                    /* Build sub-menu list */
                    var subList = document.createElement('ul');
                    subList.className = 'mobile-sub-menu';
                    var subItems = originalSub.querySelectorAll(':scope > li');
                    subItems.forEach(function (sli) {
                        var subLink = sli.querySelector('a');
                        if (subLink) {
                            var sItem = document.createElement('li');
                            sItem.className = 'mobile-nav-item';
                            var sA = document.createElement('a');
                            sA.className = 'mobile-nav-link';
                            sA.href = subLink.href;
                            sA.textContent = subLink.textContent.trim();
                            sItem.appendChild(sA);
                            subList.appendChild(sItem);

                            /* Close menu on sub-link click */
                            sA.addEventListener('click', function () { closeOverlay(); });
                        }
                    });

                    /* Append toggle + sub */
                    link.appendChild(toggle);
                    newItem.appendChild(link);
                    newItem.appendChild(subList);

                    /* Toggle click */
                    toggle.addEventListener('click', function (e) {
                        e.preventDefault();
                        e.stopPropagation();
                        var isOpen = subList.classList.contains('open');
                        subList.classList.toggle('open');
                        toggle.classList.toggle('rotated');
                    });
                } else {
                    newItem.appendChild(link);
                }

                /* Close menu on link click (no sub-menu) */
                if (!originalSub) {
                    link.addEventListener('click', function () { closeOverlay(); });
                }
            }

            navList.appendChild(newItem);
        });

        overlay.appendChild(navList);
        document.body.appendChild(overlay);

        /* ── 3. Event handlers ── */
        function openOverlay() {
            overlay.classList.add('open');
            document.body.style.overflow = 'hidden';
        }
        function closeOverlay() {
            overlay.classList.remove('open');
            document.body.style.overflow = '';
            /* Reset sub-menus */
            var openSubs = overlay.querySelectorAll('.mobile-sub-menu.open');
            for (var i = 0; i < openSubs.length; i++) openSubs[i].classList.remove('open');
            var rotated = overlay.querySelectorAll('.mobile-sub-toggle.rotated');
            for (var j = 0; j < rotated.length; j++) rotated[j].classList.remove('rotated');
        }

        hamburgerBtn.addEventListener('click', function (e) {
            e.preventDefault();
            e.stopPropagation();
            openOverlay();
        });

        closeBtn.addEventListener('click', function (e) {
            e.preventDefault();
            e.stopPropagation();
            closeOverlay();
        });

        /* Close on resize to desktop */
        window.addEventListener('resize', function () {
            if (window.innerWidth > 767) {
                closeOverlay();
            }
        });
    }

    /* ── Run ── */
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
