import os
import re

# Function to capitalize the title in frontmatter
def capitalize_title_in_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Match YAML frontmatter
    match = re.match(r"---\n(.*?)\n---\n(.*)", content, re.DOTALL)
    if not match:
        return  # Skip files without frontmatter

    frontmatter, body = match.groups()

    # Match and capitalize the title while keeping the rest of the casing
    frontmatter_updated = re.sub(
        r"(?<=title:\s)(.)",  # Match the first character after 'title:'
        lambda m: m.group(1).upper(),  # Capitalize only the first letter
        frontmatter
    )

    # Rewrite the file only if the frontmatter changes
    if frontmatter != frontmatter_updated:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"---\n{frontmatter_updated}\n---\n{body}")

# Iterate through all Markdown files in cwd
for filename in os.listdir():
    if filename.endswith('.md'):
        capitalize_title_in_markdown(filename)

print("Titles updated to start with a capital letter.")
