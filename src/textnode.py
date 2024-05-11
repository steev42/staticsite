from htmlnode import LeafNode

class TextTypes:
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    text = ""
    text_type = ""
    url = None

    def __init__(self, text, type, url=None):
        self.text = text
        self.text_type = type
        self.url = url


    def __eq__(self,node):
        if (self.text == node.text and self.text_type == node.text_type and self.url == node.url):
            return True
        return False


    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    

    def text_node_to_html_node(text_node):
        match text_node.text_type:
            case TextTypes.TEXT:
                return LeafNode(value=text_node.text)
            case TextTypes.BOLD:
                return LeafNode("b",text_node.text)
            case TextTypes.ITALIC:
                return LeafNode("i",text_node.text)
            case TextTypes.CODE:
                return LeafNode("code",text_node.text)
            case TextTypes.LINK:
                return LeafNode("a",text_node.text, {"href":text_node.url})
            case TextTypes.IMAGE:
                return LeafNode("img","",{"src":text_node.url,"alt":text_node.text})
            case _:
                raise Exception("Invalid text type format")
