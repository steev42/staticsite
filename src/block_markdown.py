from textnode import (
    TextNode,
    TextTypes
)

def markdown_to_blocks(markdown):
    blocks = []
    
    split_by_lines = markdown.split('\n')
    block = ""        
    for line in split_by_lines:
        if line == "" and block != "":
            blocks.append(block)
            block = ""
        elif line == "":
            continue
        elif block != "":
            block += '\n' + line.strip()
        else:
            block += line.strip()
    # Put in the last block
    if block != "":
        blocks.append(block)

    return blocks

