from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, properties=None):
        super().__init__(tag=tag, children=children, properties=properties)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("No tag found")
        if not self.children:
            raise ValueError("No children found")
        
        outstring = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            outstring+=child.to_html()
        outstring += f"</{self.tag}>"
        return outstring