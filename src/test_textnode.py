import unittest

from textnode import (
    TextNode,
    TextTypes
    )

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextTypes.BOLD)
        node2 = TextNode("This is a text node", TextTypes.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextTypes.BOLD)
        node2 = TextNode("Changed text", TextTypes.BOLD)
        self.assertNotEqual(node, node2)
    
        node2 = TextNode("This is a text node", TextTypes.ITALIC)
        self.assertNotEqual(node, node2)

        node2 = TextNode("This is a text node", TextTypes.BOLD, "http://localhost:8888")
        self.assertNotEqual(node, node2)

    def test_convert_to_html_text(self):
        node = TextNode("This is a normal text node", TextTypes.TEXT)
        
        # Despite having text_node as argument, this works - always passes self as first argument
        leaf = node.text_node_to_html_node() 
        self.assertEqual(leaf.to_html(), "This is a normal text node")
    
    def test_convert_to_html_bold(self):
        node = TextNode("This is a bold text node", TextTypes.BOLD)
        
        # Despite having text_node as argument, this works - always passes self as first argument
        leaf = node.text_node_to_html_node() 
        self.assertEqual(leaf.to_html(), "<b>This is a bold text node</b>")

    def test_convert_to_html_italic(self):
        node = TextNode("This is an italic text node", TextTypes.ITALIC)
        
        # Despite having text_node as argument, this works - always passes self as first argument
        leaf = node.text_node_to_html_node() 
        self.assertEqual(leaf.to_html(), "<i>This is an italic text node</i>")

    def test_convert_to_html_code(self):
        node = TextNode("This is a code text node", TextTypes.CODE)
        
        # Despite having text_node as argument, this works - always passes self as first argument
        leaf = node.text_node_to_html_node() 
        self.assertEqual(leaf.to_html(), "<code>This is a code text node</code>")

    def test_convert_to_html_link(self):
        node = TextNode("This is a link text node", TextTypes.LINK,"http://localhost:8888")
        
        # Despite having text_node as argument, this works - always passes self as first argument
        leaf = node.text_node_to_html_node() 
        self.assertEqual(leaf.to_html(), '<a href="http://localhost:8888">This is a link text node</a>')

    def test_convert_to_html_image(self):
        node = TextNode("This is an image node", TextTypes.IMAGE, "http://localhost:8888/image.jpg")
        
        # Despite having text_node as argument, this works - always passes self as first argument
        leaf = node.text_node_to_html_node() 
        self.assertEqual(leaf.to_html(), '<img src="http://localhost:8888/image.jpg" alt="This is an image node"></img>')


if __name__ == "__main__":
    unittest.main()