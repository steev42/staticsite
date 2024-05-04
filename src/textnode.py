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
    
