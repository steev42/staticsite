from static_copy import replace_public_directory
from generator import *

content_folder = "./content"
template_path = "./template.html"
dest_path = "./public"


def main():
    replace_public_directory()

    generate_pages_recursive(content_folder, template_path, dest_path)

if __name__ == "__main__":
    main()