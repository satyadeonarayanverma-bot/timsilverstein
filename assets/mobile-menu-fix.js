document.addEventListener('DOMContentLoaded', function () {
    console.log('Mobile Menu Fix Loaded (v2)');

    const toggles = document.querySelectorAll('.hfe-nav-menu__toggle');

    toggles.forEach(toggle => {
        const wrapper = toggle.closest('.hfe-nav-menu');
        const navMenu = wrapper ? wrapper.querySelector('.hfe-nav-menu__layout-horizontal') : null;

        if (!navMenu) return;

        // Icon Handling
        const iconContainer = toggle.querySelector('.hfe-nav-menu-icon');
        const iconOpen = iconContainer ? iconContainer.querySelector('svg, i') : null;
        let iconClose = null;

        // Create close icon if not present
        if (iconContainer) {
            // Check if a close icon already exists (hidden)
            // Some themes might have it. If not, create it.
            // We use a class to identify our injected icon or existing one

            // Try to find an existing close icon structure if strictly defined, otherwise inject ours
            // For simplicity and to guarantee it works, we inject ours and manage visibility
            const svgClose = document.createElementNS("http://www.w3.org/2000/svg", "svg");
            svgClose.setAttribute("aria-hidden", "true");
            svgClose.setAttribute("class", "e-font-icon-svg e-far-window-close mobile-menu-fix-close");
            svgClose.setAttribute("viewBox", "0 0 512 512");
            svgClose.innerHTML = '<path d="M464 32H48C21.5 32 0 53.5 0 80v352c0 26.5 21.5 48 48 48h416c26.5 0 48-21.5 48-48V80c0-26.5-21.5-48-48-48zm0 394c0 3.3-2.7 6-6 6H54c-3.3 0-6-2.7-6-6V86c0-3.3 2.7-6 6-6h404c3.3 0 6 2.7 6 6v340zM356.5 194.6L295.1 256l61.4 61.4c4.6 4.6 4.6 12.1 0 16.8l-22.3 22.3c-4.6 4.6-12.1 4.6-16.8 0L256 295.1l-61.4 61.4c-4.6 4.6-12.1 4.6-16.8 0l-22.3-22.3c-4.6-4.6-4.6-12.1 0-16.8l61.4-61.4-61.4-61.4c-4.6-4.6-4.6-12.1 0-16.8l22.3-22.3c4.6-4.6 12.1-4.6 16.8 0l61.4 61.4 61.4-61.4c4.6-4.6 12.1-4.6 16.8 0l22.3 22.3c4.7 4.6 4.7 12.1 0 16.8z"></path>';
            svgClose.style.display = 'none';

            iconContainer.appendChild(svgClose);
            iconClose = svgClose;
        }

        toggle.addEventListener('click', function (e) {
            e.preventDefault();

            const isExpanded = toggle.getAttribute('aria-expanded') === 'true';
            const newExpandedState = !isExpanded;

            toggle.setAttribute('aria-expanded', newExpandedState);
            toggle.classList.toggle('hfe-active');
            toggle.classList.toggle('hfe-active-menu'); // Added this class as per theme CSS

            if (newExpandedState) {
                // Show
                navMenu.style.display = 'block';
                navMenu.style.visibility = 'visible';
                navMenu.style.height = 'auto'; // Let it flow
                navMenu.style.maxHeight = 'none';
                navMenu.style.opacity = '1';

                if (iconOpen) iconOpen.style.display = 'none';
                if (iconClose) iconClose.style.display = 'block';
            } else {
                // Hide
                navMenu.style.display = 'none';
                navMenu.style.visibility = 'hidden';
                navMenu.style.height = '0';
                navMenu.style.maxHeight = '0';
                navMenu.style.opacity = '0';

                if (iconOpen) iconOpen.style.display = 'block';
                if (iconClose) iconClose.style.display = 'none';
            }
        });
    });
});
