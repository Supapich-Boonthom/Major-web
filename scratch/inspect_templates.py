# -*- coding: utf-8 -*-
with open('templates/base.html', 'r', encoding='utf-8') as f:
    base_lines = f.readlines()

part1 = base_lines[:690]
inserted = ["    {% block content %}\n", "    {% endblock %}\n"]
part3 = base_lines[3283:]

new_content = part1 + inserted + part3

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.writelines(new_content)

print("Successfully updated templates/base.html!")
