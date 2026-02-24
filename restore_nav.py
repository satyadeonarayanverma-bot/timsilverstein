import os
import glob
import re
import subprocess

def fix_navigation():
    # Find all html files in root
    root_dir = r"c:\Users\ADITYA VERMA\OneDrive\Documents\New folder (20)\altcloudaiclone"
    
    html_files = glob.glob(os.path.join(root_dir, '*.html'))
    # Also find any html files within assets
    html_files.extend(glob.glob(os.path.join(root_dir, 'assets', '*.html')))
    
    replacements_made = 0
    
    # We will match the entire <nav> block
    # Note: the nav tag has attributes: <nav itemscope="itemscope" itemtype="https://schema.org/SiteNavigationElement"> ... </nav>
    nav_pattern = re.compile(r"(<nav[^>]*itemtype=['\"]https://schema\.org/SiteNavigationElement['\"][^>]*>.*?</nav>)", re.IGNORECASE | re.DOTALL)
    
    for file_path in html_files:
        try:
            # Get the path relative to git root for `git show HEAD:path`
            rel_path = os.path.relpath(file_path, root_dir).replace('\\', '/')
            
            # 1. Get original content from GIT HEAD
            cmd = ['git', 'show', f'HEAD:{rel_path}']
            result = subprocess.run(cmd, cwd=root_dir, capture_output=True, text=True, encoding='utf-8', errors='ignore')
            if result.returncode != 0:
                print(f"Skipping {rel_path} - not in git.")
                continue
                
            original_file_content = result.stdout
            
            # 2. Extract original <nav> block
            nav_match = nav_pattern.search(original_file_content)
            if not nav_match:
                print(f"Nav not found in original {rel_path}.")
                continue
                
            original_nav = nav_match.group(1)
            fixed_nav = original_nav
            
            # 3. Apply Rebranding to the extracted original nav
            fixed_nav = fixed_nav.replace("Techflow", "Cloudiva.ai")
            fixed_nav = fixed_nav.replace("techflow", "cloudiva")
            # The removal of "Solutions" suffix
            # Actually, I rebranded "Cloudiva.ai Solutions" to "Cloudiva.ai" in a previous script!
            fixed_nav = fixed_nav.replace("Cloudiva.ai Solutions", "Cloudiva.ai")
            
            # 4. targeted removal of "About Us" dropdown and arrow!
            # The About Us link starts with `<a href="/about-us" ...` or `<a href="about-us.html" ...`
            # and contains the text "About Us".
            # It has a dropdown arrow: `<span class="hfe-menu-toggle sub-arrow hfe-menu-child-0"><i class="fa"></i></span>`
            # And it is followed by `<ul class="sub-menu">...</ul>` containing Global Delivery.
            
            # Safest way: Since we ONLY want to strip the sub-menu of "About Us", 
            # let's find the specific block for About Us using a tightly bound regex.
            # Look for `<a href="about-us.html"...>About Us...</a>` and the `ul` that immediately follows it.
            
            # Remove the dropdown arrow from the About Us link
            about_us_arrow_pattern = re.compile(r"(About\s*Us)\s*<span[^>]*class=['\"][^'\"]*sub-arrow[^>]*>.*?</span>", re.IGNORECASE | re.DOTALL)
            fixed_nav = about_us_arrow_pattern.sub(r"\1", fixed_nav)
            
            # Remove the sub-menu for About Us specifically
            # We will use string manipulation or a safer regex.
            # We know it contains 'Global Delivery'. We will find the `<ul class="sub-menu">` 
            # block that contains 'Global Delivery' and remove it.
            # A safe way: `(?s)<ul\s+class="sub-menu"[^>]*>(?:(?!<ul\s+class="sub-menu").)*?Global Delivery.*?</ul>`
            # This ensures we don't match across multiple sub-menus.
            submenu_removal = re.compile(r"<ul[^>]*class=['\"]sub-menu['\"][^>]*>(?:(?!<ul).)*?Global Delivery.*?</ul>", re.IGNORECASE | re.DOTALL)
            fixed_nav = submenu_removal.sub("", fixed_nav)
            
            # Also need to remove the "hfe-has-submenu" and "menu-item-has-children" classes from the <li> parent of About Us.
            # We'll just carefully replace those classes IF they are on the About Us <li>.
            # Actually, if we just remove the `sub-menu` block, the lack of hover items implies it's a normal link.
            # But the JavaScript might prevent clicking if `menu-item-has-children` is present.
            # So let's clean the classes around 'About Us'.
            about_us_li = re.compile(r"(<li[^>]*?menu-item-has-children[^>]*?>)\s*(<div[^>]*?>)?\s*<a[^>]*?(about-us\.html|/about-us/?)[^>]*?>\s*About Us", re.IGNORECASE)
            
            def clean_li_classes(m):
                li_tag = m.group(1)
                div_tag = m.group(2) or ""
                # remove "menu-item-has-children", "parent", "hfe-has-submenu"
                li_tag = li_tag.replace("menu-item-has-children", "").replace("parent", "").replace("hfe-has-submenu", "")
                li_tag = " ".join(li_tag.split()) # clean extra spaces
                # return the cleaned li, the div, and the rest
                rest = m.group(0)[len(m.group(1)+m.group(2) if m.group(2) else m.group(1)):]
                return f"{li_tag} {div_tag}{rest}"
                
            fixed_nav = about_us_li.sub(clean_li_classes, fixed_nav)
            
            # 5. Read the CURRENT broken file from disk
            with open(file_path, 'r', encoding='utf-8') as f:
                current_file_content = f.read()
                
            # 6. Replace the broken <nav> block with the fixed <nav> block
            # Note: The broken nav might be missing its closing tag if the regex went wild? No, the regex ended at `</ul>`, so the `<nav>` wrapper string was untouched!
            # It just gutted the inside of the `<nav>`. So we can search for the `<nav...` block in the current file.
            broken_nav_match = nav_pattern.search(current_file_content)
            
            if broken_nav_match:
                # Replace it in the file
                final_content = current_file_content[:broken_nav_match.start()] + fixed_nav + current_file_content[broken_nav_match.end():]
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(final_content)
                replacements_made += 1
                print(f"Restored navigation in {rel_path}")
            else:
                print(f"Could not find <nav> block to replace in {rel_path}.")
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            
    print(f"Total files restored: {replacements_made}")

if __name__ == "__main__":
    fix_navigation()
