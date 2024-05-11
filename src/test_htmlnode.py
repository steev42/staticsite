import unittest

from htmlnode import (HTMLNode, LeafNode, ParentNode)

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

    def test_render(self):
        node = LeafNode("p", "This is a paragraph of text")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text</p>")
    
    def test_render_with_properties(self):
        node = LeafNode("p","This is a paragraph of text",properties={"style":"font-weight:bold"})
        self.assertEqual(node.to_html(), '<p style="font-weight:bold">This is a paragraph of text</p>')

    def test_render(self):
        node = ParentNode("body",
                          [LeafNode("b","Bold Text")])
        self.assertEqual(node.to_html(), "<body><b>Bold Text</b></body>")
    
    def test_multiple_children_render(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
    
    def test_nested_parents_render(self):
        node = ParentNode(
            "body",
            [
                ParentNode("p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ]),
            ]
        )
        self.assertEqual(node.to_html(), "<body><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></body>")
    
    def test_double_paragraph_nested_parents_render(self):
        node = ParentNode(
            "body",
            [
                ParentNode("p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ]),
                ParentNode("p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ]),
            ]
        )
        self.assertEqual(node.to_html(), "<body><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></body>")

    def test_double_nested_parents_render(self):
        node = ParentNode(
            "body",
            [
                ParentNode("p",
                    [
                        ParentNode("div",[
                            LeafNode("b", "Bold text"),
                            LeafNode(None, "Normal text"),
                            LeafNode("i", "italic text"),
                            LeafNode(None, "Normal text"),
                        ]),
                    ]),
            ]
        )
        self.assertEqual(node.to_html(), "<body><p><div><b>Bold text</b>Normal text<i>italic text</i>Normal text</div></p></body>")


    def test_nested_parents_with_properties_render(self):
        node = ParentNode(
            "body",
            [
                ParentNode("p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                    {"prop1":"value1", "prop2":"value2"}
                    ),
            ]
        )
        self.assertEqual(node.to_html(), '<body><p prop1="value1" prop2="value2"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></body>')

if __name__ == "__main__":
    unittest.main()