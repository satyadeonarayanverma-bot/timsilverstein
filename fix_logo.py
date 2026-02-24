import re
file_path = r'c:\Users\ADITYA VERMA\OneDrive\Documents\New folder (20)\altcloudaiclone\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace Header and Footer logo instances
text = re.sub(
    r'>TechFlow</span>\s*<span[^>]*>Solutions</span>',
    '>Cloudiva<span style="color: #33a1fd">.ai</span>',
    text
)

# Replace other text instances
text = text.replace('At TechFlow', 'At Cloudiva.ai')
text = text.replace('2025 TechFlow', '2025 Cloudiva.ai')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)
print('Logo fixed.')
