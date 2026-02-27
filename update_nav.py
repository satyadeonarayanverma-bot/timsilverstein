import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

new_sub_menu = """<ul class="sub-menu">
													<li class="menu-item menu-item-type-custom menu-item-object-custom hfe-creative-menu">
														<a href="#" class="hfe-sub-menu-item" style="cursor: default;" onclick="event.preventDefault();">Cloud Transformation Services</a>
													</li>
													<li class="menu-item menu-item-type-custom menu-item-object-custom hfe-creative-menu">
														<a href="#" class="hfe-sub-menu-item" style="cursor: default;" onclick="event.preventDefault();">Strategy &amp; Advisory</a>
													</li>
													<li class="menu-item menu-item-type-custom menu-item-object-custom hfe-creative-menu">
														<a href="#" class="hfe-sub-menu-item" style="cursor: default;" onclick="event.preventDefault();">Cloud Migration</a>
													</li>
													<li class="menu-item menu-item-type-custom menu-item-object-custom hfe-creative-menu">
														<a href="#" class="hfe-sub-menu-item" style="cursor: default;" onclick="event.preventDefault();">Platform Modernization</a>
													</li>
													<li class="menu-item menu-item-type-custom menu-item-object-custom hfe-creative-menu">
														<a href="#" class="hfe-sub-menu-item" style="cursor: default;" onclick="event.preventDefault();">Managed Operations</a>
													</li>
												</ul>"""

pattern = re.compile(
    r'(<a[^>]*href="[^"]*(?:migration-modernization|cloudiva\.com)(?:\.html|/)[^"]*"[^>]*>\s*Migration &amp; Modernization.*?</a>\s*</div>\s*)<ul class="sub-menu">.*?</ul>',
    re.DOTALL | re.IGNORECASE
)

for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(file, 'r', encoding='utf-16') as f:
            content = f.read()

    new_content, count = pattern.subn(r'\g<1>' + new_sub_menu, content)
    
    if count > 0:
        try:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file}: {count} replacements.")
        except Exception as e:
            # Revert to original encoding
            with open(file, 'w', encoding='utf-16') as f:
                f.write(new_content)
            print(f"Updated {file} (UTF-16): {count} replacements.")
    else:
        print(f"No match found in {file}.")
