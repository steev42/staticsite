import unittest

from htmlnode import HTMLNode
class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        
        node = HTMLNode(None,None,None,{"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

        node = HTMLNode(p={"style":"font-class:bold"})
        self.assertEqual(node.props_to_html(), ' style="font-class:bold"')

        node = HTMLNode(p={"junk":"put in data", "more junk":"this is weird", "do a third":"blah", "foo": "bar"})
        self.assertEqual(node.props_to_html(), ' junk="put in data" more junk="this is weird" do a third="blah" foo="bar"')


if __name__ == "__main__":
    unittest.main()