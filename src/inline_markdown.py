from textnode import (
    TextNode,
    TextTypes
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextTypes.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextTypes.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

#def split_nodes_delimiter(old_nodes, delimiter, text_type):
#        if old_nodes is None or not old_nodes:
#            return []
#        rv = []
#        for node in old_nodes:
#            if node.text_type != TextTypes.TEXT:
#                rv.append(node)
#                continue
#            #Example text for comments later to trace (using delimiter '**'):
#            #"non bold text **bolded text** non bold text"
#            start_first_node = False
#            split_text = node.text.split(delimiter) #["non bold text ", "bolded text", " non bold text"] for example
#            if len(split_text) % 2 == 0:
#                raise Exception(f"Invalid Markdown Syntax: Missing closing delimiter {delimiter}")
#            
#            is_wanted_type = False
#            for text in split_text:
#                if len(text) == 0:
#                    is_wanted_type = not is_wanted_type
#                    continue
#                if is_wanted_type:
#                    rv.append(TextNode(text, text_type))
#                    is_wanted_type = False
#                else:
#                    rv.append(TextNode(text, TextTypes.TEXT))
#                    is_wanted_type = True
#
#        return rv