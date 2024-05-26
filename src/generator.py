from markdown_to_html import *
import os

def extract_title(markdown):
    node = markdown_to_html_node(markdown)
    title = recursive_extract_title(node)
    if title == None:
        raise Exception("Markdown requires a single # tag.")
    return title

def recursive_extract_title(node: HTMLNode):
    if node.tag == "h1":
        if node.children == None:
            return None
        if len(node.children) == 1:
            return node.children[0].value
        if len(node.children > 1):
            return None # This will eventually raise an Exception; there's no way this should happen!
    if node.children == None:
        return None
    if len(node.children) == 0:
        return None
    for child in node.children:
        child_title = recursive_extract_title(child)
        if child_title != None:
            return child_title
    return None

def generate_page(from_path, template_path, dest_path):
    print (f"Generating page from {from_path} to {dest_path} using {template_path}.")
    
    with open(from_path) as from_file:
        from_text = from_file.read()

    with open(template_path) as template_file:
        template_text = template_file.read()
    
    out_text = template_text.replace("{{ Title }}",extract_title(from_text))
    out_text = out_text.replace("{{ Content }}", markdown_to_html_node(from_text).to_html())

    if os.path.exists(os.path.dirname(dest_path)) == False:
        os.makedirs(os.path.dirname(dest_path))
    
    with open(dest_path, "w") as dest_file:
        dest_file.write(out_text)
    
    # Just in case
    from_file.close()
    template_file.close()
    dest_file.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    print ("Recursively generating content.")
    print (f"Source directory is {dir_path_content}")
    files = os.listdir(dir_path_content)
    print (f"{len(files)} files found")
    for file in files:
        full_file_path = os.path.join(dir_path_content, file)
        dest_file_path = os.path.join(dest_dir_path, file)
        if os.path.isfile(full_file_path):
            filename = file.split(".")[0] 
            dest_filename = filename + ".html"
            dest_full_path = os.path.join(dest_dir_path, dest_filename)
            generate_page(full_file_path, template_path, dest_full_path)

        if os.path.isdir(full_file_path):
            print (f"{full_file_path} is a directory; recursing")
            generate_pages_recursive(full_file_path, template_path, dest_file_path)
        
                          
    

    pass