#!/bin/env python3
import os

import urllib

directory = "./.public"  

readme = "./src/markdown/index.md"

start_tag = "<!-- START LINKS -->"
end_tag = "<!-- END LINKS -->"

with open(readme, "r") as file:
    readme_content = file.readlines()

links = []
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        link_text = os.path.splitext(filename)[0]
        encoded_filename = urllib.parse.quote(filename)
        link = f"- [{link_text}]({directory}/{encoded_filename})"
        links.append(link)

links_content = "\n".join(links)

start_index = None
end_index = None

# Look for the start and end tags
for i, line in enumerate(readme_content):
    if start_tag in line:
        start_index = i
    elif end_tag in line:
        end_index = i

if start_index is not None and end_index is not None:
    # Remove content between start and end tags
    readme_content = readme_content[:start_index + 1] + [f"{start_tag}\n"] + [f"## File Links\n\n{links_content}\n"] + [f"{end_tag}\n"] + readme_content[end_index:]

else:
    # append the new section
    readme_content.append("\n" + start_tag + "\n")
    readme_content.append(f"## File Links\n\n{links_content}\n")
    readme_content.append(end_tag + "\n")

with open(readme, "w") as file:
    file.writelines(readme_content)

print("Link generation complete. Check your README.md file.")
