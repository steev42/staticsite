class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, properties=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = properties
    
    def to_html(self):
        raise NotImplementedError("to_html not implemented. Use child class.")

    def props_to_html(self):
        outstring = ""
        if self.props:
            for prop in self.props:
                outstring += f' {prop}="{self.props[prop]}"'
        return outstring

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value="", properties=None):
        super().__init__(tag=tag, value=value, properties=properties)
    
    def to_html(self):
        if not self.value:
            raise ValueError("Node has no value")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

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