import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
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