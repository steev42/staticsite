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