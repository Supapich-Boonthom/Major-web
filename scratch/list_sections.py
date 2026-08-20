import re

with open('templates/base.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("Sections found in templates/base.html:")
for match in re.finditer(r'<section([^>]*id="([^"]+)"[^>]*)>', content):
    print(f"Tag: <section {match.group(1)}>, ID: {match.group(2)}")

print("\nSections found in templates/index.html:")
with open('templates/index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

for match in re.finditer(r'<section([^>]*id="([^"]+)"[^>]*)>', idx_content):
    print(f"Tag: <section {match.group(1)}>, ID: {match.group(2)}")
