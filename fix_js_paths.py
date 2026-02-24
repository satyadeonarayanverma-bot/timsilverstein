import os
import re
import glob

base_dir = r'c:\Users\ADITYA VERMA\OneDrive\Documents\New folder (20)\altcloudaiclone'
assets_dir = os.path.join(base_dir, 'assets')
html_files = glob.glob(os.path.join(base_dir, '*.html'))

# 1. Get a list of all actual JS files in the assets directory
actual_js_files = [f for f in os.listdir(assets_dir) if f.endswith('.js')]

def find_replacement_file(target_filename):
    """Finds the actual filename in assets/ based on the suffix (e.g. jquery.sticky.min.js)"""
    # Exclude the prefix hash to just get the core filename
    parts = target_filename.split('_', 1)
    if len(parts) > 1:
        core_name = parts[1]
    else:
        core_name = target_filename
        
    for actual_file in actual_js_files:
        if actual_file.endswith(core_name):
            return "assets/" + actual_file
    return None

def fix_html_file(filepath):
    # Handle UTF-8 encoding errors aggressively
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        print(f"Failed to read {os.path.basename(filepath)}: {e}")
        return

    # Find all <script src="assets/..."> tags
    # regex matches: src="assets/something.js"
    pattern = r'src="assets/([^"]+\.js)"'
    
    def replacer(match):
        old_filename = match.group(1)
        new_path = find_replacement_file(old_filename)
        if new_path:
            return f'src="{new_path}"'
        else:
            print(f"Warning: Could not find actual file for {old_filename}")
            return match.group(0)

    new_content = re.sub(pattern, replacer, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8', errors='ignore') as f:
            f.write(new_content)
        print(f"Updated JS paths in {os.path.basename(filepath)}")
    else:
        print(f"No JS paths needed updating in {os.path.basename(filepath)}")

for html_file in html_files:
    fix_html_file(html_file)
