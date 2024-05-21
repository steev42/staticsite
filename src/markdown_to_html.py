from htmlnode import *
from inline_markdown import *
from block_markdown import *
from textnode import *

def get_child_html_nodes(markdown):
    nodes = []
    text_nodes = text_to_textnodes(markdown)
    for text_node in text_nodes:
        html_node = text_node.text_node_to_html_node()
        nodes.append(html_node)
    return nodes

def markdown_to_code_node(markdown):
    #Remove block markings
    clean = markdown[3:-3]
    lines = clean.split("\n")
    paragraph = " ".join(lines)
    nodes = get_child_html_nodes(paragraph)
    innernode = ParentNode("code", nodes)
    outernode = ParentNode("pre", [innernode])
    return outernode

def markdown_to_quote_node(markdown):
    lines = markdown.split("\n")
    newlines = []
    for line in lines:
        clean = line[1:]
        newlines.append(clean.strip())
    paragraph = " ".join(newlines)
    nodes = get_child_html_nodes(paragraph)
    node = ParentNode("blockquote", nodes)
    return node

def markdown_to_unordered_list_node(markdown):
    lines = markdown.split("\n")
    nodes = []
    for line in lines:
        clean = line[2:]
        children = get_child_html_nodes(clean)
        nodes.append(ParentNode("li", children))
    node = ParentNode("ul", nodes)
    return node

def markdown_to_ordered_list_node(markdown):
    lines = markdown.split("\n")
    nodes = []
    for line in lines:
        split = line.split(". ",1)
        clean = split[1] # Get the second part, removing the "##. " of the line.
        children = get_child_html_nodes(clean)
        nodes.append(ParentNode("li", children))
    node = ParentNode("ol", nodes)
    return node

def markdown_to_header_node(markdown):
    length = len(markdown)
    stripped = markdown.lstrip("#")
    headerlevel = length - len(stripped)

    lines = stripped[1:].split("\n") 
    paragraph = " ".join(lines)
    nodes = get_child_html_nodes(paragraph)
    node = ParentNode(f"h{headerlevel}", nodes)
    return node
    # Removing the extra space from the header markdown before splitting
    #nodes = []
    
    #for line in lines:
        #line = line + " "
    #    linenodes = text_to_textnodes(line)
    #    for ln in linenodes:
    #        nodes.append(ln.text_node_to_html_node())
    
    #return ParentNode(f"h{headerlevel}", nodes)
    

def markdown_to_paragraph_node(markdown):
    lines = markdown.split("\n")
    paragraph = " ".join(lines)
    nodes = get_child_html_nodes(paragraph)
    node = ParentNode("p", nodes)
    return node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    # Split into blocks
    # Note that blocks haven't removed markdown tags
    # Figure out the block, and put outer tags
    # Each line goes text to textnodes
    for block in blocks:
        block_type = block_to_block_type(block) 
        match block_type:
            case BlockTypes.QUOTE:
                nodes.append(markdown_to_quote_node(block))
            case BlockTypes.CODE:
                nodes.append(markdown_to_code_node(block))
            case BlockTypes.UNORDERED:
                nodes.append(markdown_to_unordered_list_node(block))
            case BlockTypes.ORDERED:
                nodes.append(markdown_to_ordered_list_node(block))
            case BlockTypes.HEADING:
                nodes.append(markdown_to_header_node(block))
            case BlockTypes.PARAGRAPH:
                nodes.append(markdown_to_paragraph_node(block))
            case _:
                nodes.append(markdown_to_paragraph_node(block))
    
    node = ParentNode("div",nodes)
    
    return node    
    # markdown_to_blocks - split text into multi-line blocks
    # block_to_block_type - determine type of block
    # Missing a step - block into individual lines...
    # text_to_textnodes - Text lines split into list of TextNodes
    # text_node_to_html_node - a single text node made into a LeafNode