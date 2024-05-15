from textnode import (
    TextNode,
    TextTypes
)
import re

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


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    # gives list of tuples in response ["(group1, group2)", "(group1, group2)", ...]


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        found_links = extract_markdown_images(old_node.text)
        search_text = old_node.text
        if len(found_links) == 0:
            new_nodes.append(old_node)
            continue

        for i in range(len(found_links)):
            if len(search_text) == 0:
                break
            sections = search_text.split(f'![{found_links[i][0]}]({found_links[i][1]})',1)
            if sections[0] == "":
                new_nodes.append(TextNode(found_links[i][0], TextTypes.IMAGE, found_links[i][1]))
            else:
                new_nodes.append(TextNode(sections[0], TextTypes.TEXT))
                new_nodes.append(TextNode(found_links[i][0], TextTypes.IMAGE, found_links[i][1]))
            
            if i == len(found_links)- 1 and len(sections[1]) > 0:
                # Last loop, so append the rest as a text node.
                new_nodes.append(TextNode(sections[1], TextTypes.TEXT))
            else:
                # otherwise, make sure we're only going to be looking in the section we haven't parsed already.
                search_text = sections[1]
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        found_links = extract_markdown_links(old_node.text)
        search_text = old_node.text
        if len(found_links) == 0:
            new_nodes.append(old_node)
            continue

        for i in range(len(found_links)):
            if len(search_text) == 0:
                break
            sections = search_text.split(f'[{found_links[i][0]}]({found_links[i][1]})',1)
            if sections[0] == "":
                new_nodes.append(TextNode(found_links[i][0], TextTypes.LINK, found_links[i][1]))
            else:
                new_nodes.append(TextNode(sections[0], TextTypes.TEXT))
                new_nodes.append(TextNode(found_links[i][0], TextTypes.LINK, found_links[i][1]))
            
            if i == len(found_links) - 1  and len(sections[1]) > 0:
                # Last loop, so append the rest as a text node.
                new_nodes.append(TextNode(sections[1], TextTypes.TEXT))
            else:
                # otherwise, make sure we're only going to be looking in the section we haven't parsed already.
                search_text = sections[1]
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextTypes.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextTypes.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextTypes.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextTypes.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes