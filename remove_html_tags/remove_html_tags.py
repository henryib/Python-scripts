import re
import sys

print("Usage: python remove_html_tags.py <html_file> <tag_to_remove>")
def remove_html_tags(html_file, tag):
    try:
        # Read the HTML file
        with open(html_file, 'r') as file:
            html_content = file.read()

        # Define the regular expression pattern based on the specified tag
        pattern = fr'<{tag}>(.*?)<\/{tag}>'

        # Use regular expressions to remove the specified tag and its contents
        html_content = re.sub(pattern, r'\1', html_content)

        # Write the modified content back to the HTML file
        with open(html_file, 'w') as file:
            file.write(html_content)

        print(f"Removed <{tag}> and </{tag}> tags from {html_file}")
    except FileNotFoundError:
        print(f"File not found: {html_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python remove_html_tags.py <html_file> <tag_to_remove>")
    else:
        html_file = sys.argv[1]
        tag_to_remove = sys.argv[2]
        remove_html_tags(html_file, tag_to_remove)
