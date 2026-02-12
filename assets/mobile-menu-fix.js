/**
 * Mobile Menu Fix v3 – Bulletproof hamburger menu for all pages
 * Uses direct inline style manipulation to bypass any CSS specificity issues
 */
(function () {
    'use strict';

    /* ── 0. Inject critical CSS overrides with maximum specificity ── */
    var style = document.createElement('style');
    style.id = 'mobile-menu-fix-styles';
    style.textContent = [
        '@media only screen and (max-width: 767px) {',
        /* Force hamburger visible - ultra specific selectors */
        '  .hfe-layout-horizontal .hfe-nav-menu__toggle,',
        '  .hfe-layout-vertical .hfe-nav-menu__toggle,',
        '  .hfe-nav-menu .hfe-nav-menu__toggle,',
        '  div.hfe-nav-menu__toggle.elementor-clickable,',
        '  div.hfe-nav-menu__toggle {',
        '    visibility: visible !important;',
        '    opacity: 1 !important;',
        '    display: flex !important;',
        '    cursor: pointer;',
        '    padding: 8px;',
        '    margin-left: auto;',
        '    z-index: 10000;',
        '    align-items: center;',
        '    position: relative;',
        '  }',
        '  .hfe-nav-menu__toggle .hfe-nav-menu-icon {',
        '    display: flex !important;',
        '    align-items: center;',
        '  }',
        '  .hfe-nav-menu__toggle .hfe-nav-menu-icon svg {',
        '    width: 28px !important;',
        '    height: 28px !important;',
        '    fill: #ffffff !important;',
        '    display: block !important;',
        '  }',
        /* Hide horizontal nav by default on mobile */
        '  nav.hfe-nav-menu__layout-horizontal {',
        '    display: none !important;',
        '    visibility: hidden !important;',
        '    opacity: 0 !important;',
        '    height: 0 !important;',
        '    overflow: hidden !important;',
        '  }',
        /* When menu is open */
        '  nav.hfe-nav-menu__layout-horizontal.mobile-menu-open {',
        '    display: block !important;',
        '    visibility: visible !important;',
        '    opacity: 1 !important;',
        '    height: auto !important;',
        '    overflow: visible !important;',
        '    position: absolute !important;',
        '    top: 100% !important;',
        '    left: 0 !important;',
        '    right: 0 !important;',
        '    width: 100vw !important;',
        '    background: #0a0a0a !important;',
        '    z-index: 9999 !important;',
        '    padding: 10px 0 !important;',
        '    box-shadow: 0 8px 24px rgba(0,0,0,0.4) !important;',
        '    animation: mobileMenuSlide 0.25s ease-out;',
        '  }',
        '  @keyframes mobileMenuSlide {',
        '    from { opacity: 0; transform: translateY(-10px); }',
        '    to   { opacity: 1; transform: translateY(0); }',
        '  }',
        /* Stack menu items vertically */
        '  nav.mobile-menu-open ul.hfe-nav-menu {',
        '    display: flex !important;',
        '    flex-direction: column !important;',
        '    width: 100% !important;',
        '    flex-wrap: nowrap !important;',
        '  }',
        '  nav.mobile-menu-open li.menu-item {',
        '    width: 100% !important;',
        '    border-bottom: 1px solid rgba(255,255,255,0.08);',
        '  }',
        '  nav.mobile-menu-open li.menu-item:last-child {',
        '    border-bottom: none;',
        '  }',
        '  nav.mobile-menu-open li a.hfe-menu-item {',
        '    padding: 14px 20px !important;',
        '    color: #ffffff !important;',
        '    font-size: 15px !important;',
        '    display: flex !important;',
        '    justify-content: space-between !important;',
        '    align-items: center !important;',
        '  }',
        '  nav.mobile-menu-open li a.hfe-menu-item:hover {',
        '    background: rgba(255,255,255,0.06);',
        '  }',
        /* Sub-menu styling */
        '  nav.mobile-menu-open .sub-menu {',
        '    position: static !important;',
        '    visibility: hidden !important;',
        '    opacity: 0 !important;',
        '    height: 0 !important;',
        '    overflow: hidden !important;',
        '    width: 100% !important;',
        '    background: rgba(255,255,255,0.03) !important;',
        '    box-shadow: none !important;',
        '    transition: none !important;',
        '    min-width: unset !important;',
        '  }',
        '  nav.mobile-menu-open .sub-menu.mobile-sub-open {',
        '    visibility: visible !important;',
        '    opacity: 1 !important;',
        '    height: auto !important;',
        '    overflow: visible !important;',
        '    padding: 0 !important;',
        '    display: block !important;',
        '  }',
        '  nav.mobile-menu-open .sub-menu a.hfe-sub-menu-item {',
        '    padding: 12px 20px 12px 36px !important;',
        '    color: #b0b0b0 !important;',
        '    font-size: 14px !important;',
        '    display: block !important;',
        '  }',
        '  nav.mobile-menu-open .sub-menu a.hfe-sub-menu-item:hover {',
        '    color: #ffffff !important;',
        '    background: rgba(255,255,255,0.04);',
        '  }',
        /* Sub-arrow indicator */
        '  nav.mobile-menu-open .hfe-menu-toggle.sub-arrow {',
        '    display: flex !important;',
        '    padding: 10px 16px !important;',
        '    cursor: pointer;',
        '    transition: transform 0.2s ease;',
        '  }',
        '  nav.mobile-menu-open .hfe-menu-toggle.sub-arrow.rotated {',
        '    transform: rotate(180deg);',
        '  }',
        '  nav.mobile-menu-open .hfe-menu-toggle.sub-arrow i.fa::before {',
        '    content: "▾" !important;',
        '    font-family: inherit !important;',
        '    color: #888 !important;',
        '    font-size: 14px !important;',
        '    font-style: normal !important;',
        '  }',
        /* Header container position for absolute dropdown */
        '  .e-con.e-parent[data-settings*="sticky"] {',
        '    position: relative !important;',
        '  }',
        '  .e-con-inner {',
        '    position: relative !important;',
        '  }',
        '}',
        /* Desktop: force normal display */
        '@media only screen and (min-width: 768px) {',
        '  div.hfe-nav-menu__toggle {',
        '    display: none !important;',
        '  }',
        '  nav.hfe-nav-menu__layout-horizontal {',
        '    display: block !important;',
        '    visibility: visible !important;',
        '    opacity: 1 !important;',
        '    height: auto !important;',
        '  }',
        '}'
    ].join('\n');
    document.head.appendChild(style);

    /* ── 1. Run on DOM ready ── */
    function initMobileMenu() {

        var toggles = document.querySelectorAll('.hfe-nav-menu__toggle');
        if (!toggles.length) return;

        toggles.forEach(function (toggle) {

            /* Also force visibility via inline style as ultimate override */
            if (window.innerWidth <= 767) {
                toggle.style.setProperty('display', 'flex', 'important');
                toggle.style.setProperty('visibility', 'visible', 'important');
                toggle.style.setProperty('opacity', '1', 'important');
            }

            var wrapper = toggle.closest('.hfe-nav-menu') ||
                toggle.closest('.elementor-widget-container');
            if (!wrapper) return;

            var navMenu = wrapper.querySelector('nav.hfe-nav-menu__layout-horizontal') ||
                wrapper.querySelector('nav');
            if (!navMenu) return;

            /* Icon references */
            var iconContainer = toggle.querySelector('.hfe-nav-menu-icon');
            var openIcon = iconContainer ? iconContainer.querySelector('svg.e-fas-align-justify') : null;

            /* Create close (X) icon if not already present */
            var closeIcon = iconContainer ? iconContainer.querySelector('.mobile-menu-close-icon') : null;
            if (!closeIcon && iconContainer) {
                closeIcon = document.createElementNS("http://www.w3.org/2000/svg", "svg");
                closeIcon.setAttribute("aria-hidden", "true");
                closeIcon.setAttribute("class", "e-font-icon-svg mobile-menu-close-icon");
                closeIcon.setAttribute("viewBox", "0 0 352 512");
                closeIcon.setAttribute("style", "width:22px;height:22px;fill:#ffffff;display:none;");
                closeIcon.innerHTML = '<path d="M242.72 256l100.07-100.07c12.28-12.28 12.28-32.19 0-44.48l-22.24-22.24c-12.28-12.28-32.19-12.28-44.48 0L176 189.28 75.93 89.21c-12.28-12.28-32.19-12.28-44.48 0L9.21 111.45c-12.28 12.28-12.28 32.19 0 44.48L109.28 256 9.21 356.07c-12.28 12.28-12.28 32.19 0 44.48l22.24 22.24c12.28 12.28 32.19 12.28 44.48 0L176 322.72l100.07 100.07c12.28 12.28 32.19 12.28 44.48 0l22.24-22.24c12.28-12.28 12.28-32.19 0-44.48L242.72 256z"></path>';
                iconContainer.appendChild(closeIcon);
            }

            var isOpen = false;

            /* ── Toggle click handler ── */
            toggle.addEventListener('click', function (e) {
                e.preventDefault();
                e.stopPropagation();

                isOpen = !isOpen;

                if (isOpen) {
                    navMenu.classList.add('mobile-menu-open');
                    toggle.classList.add('hfe-active', 'hfe-active-menu');
                    if (openIcon) openIcon.style.display = 'none';
                    if (closeIcon) closeIcon.style.display = 'block';
                } else {
                    closeMenu();
                }
            });

            function closeMenu() {
                isOpen = false;
                navMenu.classList.remove('mobile-menu-open');
                toggle.classList.remove('hfe-active', 'hfe-active-menu');
                if (openIcon) openIcon.style.display = 'block';
                if (closeIcon) closeIcon.style.display = 'none';

                /* Close all sub-menus */
                var openSubs = navMenu.querySelectorAll('.sub-menu.mobile-sub-open');
                for (var i = 0; i < openSubs.length; i++) {
                    openSubs[i].classList.remove('mobile-sub-open');
                }
                var rotatedArrows = navMenu.querySelectorAll('.sub-arrow.rotated');
                for (var j = 0; j < rotatedArrows.length; j++) {
                    rotatedArrows[j].classList.remove('rotated');
                }
            }

            /* ── Sub-menu toggle logic ── */
            var subArrows = wrapper.querySelectorAll('.hfe-menu-toggle.sub-arrow');
            subArrows.forEach(function (arrow) {
                arrow.addEventListener('click', function (e) {
                    e.preventDefault();
                    e.stopPropagation();

                    var parentLi = arrow.closest('li.hfe-has-submenu') || arrow.closest('li.menu-item-has-children');
                    if (!parentLi) return;

                    var subMenu = parentLi.querySelector('.sub-menu');
                    if (!subMenu) return;

                    if (subMenu.classList.contains('mobile-sub-open')) {
                        subMenu.classList.remove('mobile-sub-open');
                        arrow.classList.remove('rotated');
                    } else {
                        subMenu.classList.add('mobile-sub-open');
                        arrow.classList.add('rotated');
                    }
                });
            });

            /* ── Close menu on outside click ── */
            document.addEventListener('click', function (e) {
                if (isOpen && !wrapper.contains(e.target)) {
                    closeMenu();
                }
            });

            /* ── Resize handler ── */
            window.addEventListener('resize', function () {
                if (window.innerWidth > 767 && isOpen) {
                    closeMenu();
                }
                /* Re-apply inline styles on resize */
                if (window.innerWidth <= 767) {
                    toggle.style.setProperty('display', 'flex', 'important');
                    toggle.style.setProperty('visibility', 'visible', 'important');
                    toggle.style.setProperty('opacity', '1', 'important');
                } else {
                    toggle.style.removeProperty('display');
                    toggle.style.removeProperty('visibility');
                    toggle.style.removeProperty('opacity');
                }
            });
        });
    }

    /* Run immediately if DOM already loaded, otherwise wait */
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initMobileMenu);
    } else {
        initMobileMenu();
    }
})();
