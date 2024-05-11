class HTMLNode:

    tag = ""
    value = ""
    children  = []
    props = {}

    def __init__(self, tag=None, value=None, children=None, properties=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = properties
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        outstring = ""
        if self.props:
            for prop in self.props.keys():
                outstring += (" " + prop + "=\"" + self.props[prop] + "\"")
        return outstring

    def __repr__(self):
        outstring = "{"
        if self.tag:
            outstring += self.tag + ", "
        else:
            outstring += "None, "
        if self.value:
            outstring += self.value +", "
        else:
            outstring += "None, "
        if self.children:
            outstring += self.children + ", "
        else:
            outstring += "None, "
        if self.props:
            outstring += self.props_to_html()
        else:
            outstring += "None"
        outstring += "}"
        return f"HTMLNode({outstring})"
    