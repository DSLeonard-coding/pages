#!/bin/env python3
#DSLStaticWebBuild, Doug Leonard, 2024, MIT.
import os
import subprocess
import glob
import webbrowser
import pypandoc
from scripts.add_links import add_links


def convert_and_open_notebooks(source_dir, output_dir):
    """Converts notebooks and opens HTML in browser."""

    # Construct the absolute output directory path relative to the current working directory
    abs_output_dir = os.path.abspath(output_dir)

    if not os.path.exists(abs_output_dir):
        os.makedirs(abs_output_dir)

    notebook_files = glob.glob(os.path.join(source_dir, "*.ipynb"))

    if not notebook_files:
        print(f"No notebooks found in {source_dir}")
        return

    html_files_to_open = []

    for notebook_file in notebook_files:
        try:
            notebook_name = os.path.splitext(os.path.basename(notebook_file))[0]

            # Construct the output file path using the absolute output directory
            output_file = os.path.join(abs_output_dir, f"{notebook_name}.html")

            command = [
                "jupyter",
                "nbconvert",
                "--to",
                "html",
                "--output",
                output_file,
                notebook_file,
            ]

            process = subprocess.Popen(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            stdout, stderr = process.communicate()

            if process.returncode != 0:
                print(f"Error converting {notebook_file} (return code: {process.returncode}):")
                print(stderr.decode())
            else:
                print(f"Converted {notebook_file} to {output_file}")
                html_files_to_open.append(output_file)

        except Exception as e:
            print(f"An unexpected error occurred with {notebook_file}: {e}")

    if html_files_to_open:
        print("Opening converted notebooks in browser...")
        for html_file in html_files_to_open:
            webbrowser.open("file://" + os.path.abspath(html_file))
    else:
        print("No files converted successfully, nothing to open.")

def markdownToHtml(input_dir, output_dir):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Loop through all markdown files in the input directory
    for markdown_file in os.listdir(input_dir):
        if markdown_file.endswith('.md'):
            # Full path to the markdown file
            markdown_path = os.path.join(input_dir, markdown_file)
            
            # Extract the base name (without extension)
            base_name = os.path.splitext(markdown_file)[0]
            
            # Define the output file path (you can change the format here, e.g., .html, .pdf, etc.)
            output_file = os.path.join(output_dir, f'{base_name}.html')
            
            # Convert using pypandoc
            pypandoc.convert_file(markdown_path, 'html',format='markdown_github', outputfile=output_file)
            
            print(f"Converted {markdown_path} to {output_file}")

            print("Opening converted markdown in browser...")
            webbrowser.open("file://" + os.path.abspath(output_file))

if __name__ == "__main__":

    output_directory = "public"  # Relative to the project root
    # Now notebooks
    source_directory = "src/notebooks"
    convert_and_open_notebooks(source_directory, output_directory)
    print("Conversion and opening process finished.")

    ##add_links.add_links()
    #Parse markdown
    source_directory = "src/markdown"
    markdownToHtml(source_directory, output_directory)
