from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value="", properties=None):
        super().__init__(tag=tag, value=value, properties=properties)
    
    def to_html(self):
        if not self.value:
            raise ValueError("Node has no value")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


