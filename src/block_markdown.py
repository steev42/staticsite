from textnode import (
    TextNode,
    TextTypes
)

class BlockTypes:
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED = "unordered"
    ORDERED = "ordered"

import re

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

def block_to_block_type(block):
    
    if re.fullmatch(r"#{1,6} .*", block, re.DOTALL) != None:
        return BlockTypes.HEADING
    if re.fullmatch(r"```.*```", block, re.DOTALL) != None:
        return BlockTypes.CODE
    
    matching_quote = True
    matching_unordered = True
    matching_ordered = True

    lines = block.split('\n')

    for i in range(len(lines)):
        if lines[i].startswith(">") == False:
            matching_quote = False
        if lines[i].startswith("* ") == False and lines[i].startswith("- ") == False:
            matching_unordered = False
        if (lines[i].startswith(f"{i+1}. ")) == False:
            matching_ordered = False
        if not (matching_ordered or matching_unordered or matching_quote):
            break
    
    if matching_quote:
        return BlockTypes.QUOTE
    if matching_unordered:
        return BlockTypes.UNORDERED
    if matching_ordered:
        return BlockTypes.ORDERED
    
    return BlockTypes.PARAGRAPH