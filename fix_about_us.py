import os
import re

path = r'c:\Users\ADITYA VERMA\OneDrive\Documents\New folder (20)\altcloudaiclone\about-us.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# The content we want to keep ends exactly at the closing </style> tag.
split1 = text.find('</style>') + 8
if split1 == 7:
    print('Error: Could not find </style>')
    exit(1)

# Find the resumption point (the javascript bundle)
resumption_str = '<script type="speculationrules">'
split2 = text.find(resumption_str)

if split2 == -1:
    print('Error: Could not find speculationrules script block')
    exit(1)

resumption_text = text[split2:]

# remove footer from resumption text
final_text = text[:split1] + '\n\t\t\t\t\t</div><!-- .futurio-content -->\n\t\t\t\t</div><!-- .post -->\n\t\t\t</article>\n\t\t</div><!-- .row -->\n\t</div><!-- .page-area -->\n</div><!-- .main-container -->\n' + re.sub(r'<footer.*?</footer>', '', resumption_text, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(final_text)

print('Successfully scrubbed old content and footer from about-us.html')
