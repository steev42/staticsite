import unittest

from htmlnode import HTMLNode
class TestHTMLNode(unittest.TestCase):
    def test_empty_props(self):

        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_with_earlier_defined_parameters(self):
        node = HTMLNode(None,None,None,{"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
    
    def test_props_with_declared_properties(self):
        node = HTMLNode(properties={"style":"font-class:bold"})
        self.assertEqual(node.props_to_html(), ' style="font-class:bold"')
    
    def test_props_with_spaced_and_junk_data(self):
        node = HTMLNode(properties={"junk":"put in data", "more junk":"this is weird", "do a third":"blah", "foo": "bar"})
        self.assertEqual(node.props_to_html(), ' junk="put in data" more junk="this is weird" do a third="blah" foo="bar"')


if __name__ == "__main__":
    unittest.main()