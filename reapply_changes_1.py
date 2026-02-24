import os
import glob
import re

def reapply_changes():
    root_dir = r"c:\Users\ADITYA VERMA\OneDrive\Documents\New folder (20)\altcloudaiclone"
    html_files = glob.glob(os.path.join(root_dir, '*.html'))
    html_files.extend(glob.glob(os.path.join(root_dir, 'assets', '*.html')))
    css_files = glob.glob(os.path.join(root_dir, 'assets', '*.css'))
    all_files = html_files + css_files
    
    # 1. Rebrand text and SVG
    for file_path in all_files:
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except Exception as e:
            print(f"Skipping {file_path}: {e}")
            continue
        
        orig = content
        
        # Exact replacements from earlier
        content = content.replace("Techflow", "Cloudiva.ai")
        content = content.replace("techflow", "cloudiva")
        
        # Remove the 'Solutions' suffix from the brand
        content = content.replace("Cloudiva.ai Solutions", "Cloudiva.ai")
        content = content.replace("cloudiva solutions", "cloudiva")
        content = content.replace("TechFlow Solutions", "Cloudiva.ai")
        
        # The SVG filename update
        content = content.replace("techflow_logo.svg", "cloudiva_logo.svg")
        
        # 2. Fix the "About Us" sub-menu dropdown (the origin of the bug)
        if file_path.endswith('.html'):
            # This time, we pinpoint the precise pattern:
            # We find the <li> that contains the "About Us" link, and we carefully strip the classes + arrow + sub-menu
            
            # Step A: Remove the dropdown arrow from the About Us link
            # Match: `<span class="hfe-menu-toggle sub-arrow hfe-menu-child-0"><i class="fa"></i></span>` inside the About Us link
            about_us_arrow_pattern = re.compile(r"(href=['\"][^'\"]*about-us\.html[^'\"]*['\"][^>]*>About Us)\s*<span[^>]*class=['\"]hfe-menu-toggle[^>]*>.*?</span>", re.IGNORECASE | re.DOTALL)
            content = about_us_arrow_pattern.sub(r"\1", content)
            
            # Step B: Remove the <ul class="sub-menu">...</ul> that follows the About Us link.
            # We know the About Us link is in a `<div class="hfe-has-submenu-container"` ... `</div>`
            # and right after that `</div>` comes the `<ul class="sub-menu">` with Global Delivery.
            # So let's delete exactly that sequence:
            ul_pattern = re.compile(r"(>About Us</a>.*?</div>)\s*<ul[^>]*class=['\"]sub-menu['\"][^>]*>.*?Global Delivery.*?</ul>", re.IGNORECASE | re.DOTALL)
            content = ul_pattern.sub(r"\1", content)
            
            # Step C: Removing the classes from the parent <li> wrapper
            # It looks like: `<li id="menu-item-801" itemprop="name" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children parent hfe-has-submenu hfe-creative-menu">`
            # Let's replace those "has-children" classes for ALL <li> containing an about-us link
            li_cleaner = re.compile(r"(<li[^>]*?class=['\"][^'\"]*)(menu-item-has-children\s*parent\s*hfe-has-submenu\s*)([^'\"]*['\"][^>]*>\s*<div[^>]*>\s*<a[^>]*about-us\.html)", re.IGNORECASE)
            content = li_cleaner.sub(r"\1\3", content)
            
            # Another variant in mobile menu might just have those classes
            li_cleaner2 = re.compile(r"(<li[^>]*?class=['\"][^'\"]*)(current-menu-ancestor\s*current-menu-parent\s*current_page_parent\s*current_page_ancestor\s*menu-item-has-children\s*parent\s*hfe-has-submenu\s*)([^'\"]*['\"][^>]*>\s*<div[^>]*>\s*<a[^>]*about-us\.html)", re.IGNORECASE)
            content = li_cleaner2.sub(r"\1\3", content)

        if orig != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {os.path.basename(file_path)}")

if __name__ == "__main__":
    reapply_changes()
