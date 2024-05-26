from static_copy import replace_public_directory
from markdown_to_html import generate_page


def main():
    replace_public_directory()

    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()