import unittest

from leafnode import LeafNode
class TestLeafNode(unittest.TestCase):
    def test_render(self):
        node = LeafNode("p", "This is a paragraph of text")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text</p>")
    
    def test_render_with_properties(self):
        node = LeafNode("p","This is a paragraph of text",properties={"style":"font-weight:bold"})
        self.assertEqual(node.to_html(), '<p style="font-weight:bold">This is a paragraph of text</p>')

if __name__ == "__main__":
    unittest.main()