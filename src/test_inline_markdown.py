import unittest

from textnode import (
    TextNode,
    TextTypes
    )

from inline_markdown import split_nodes_delimiter

class TestInlineMarkdown(unittest.TestCase):

    def test_split_by_delimiter(self):
        node = TextNode("Splitting on **bold text** to get three items.", TextTypes.TEXT)
        split = split_nodes_delimiter([node], "**", TextTypes.BOLD)
        self.assertEqual(split, [TextNode("Splitting on ", TextTypes.TEXT),
                                 TextNode("bold text", TextTypes.BOLD),
                                 TextNode(" to get three items.", TextTypes.TEXT)])
    
    def test_split_by_starting_delimiter(self):
        node = TextNode("**Start with bold** text, then go to plain.", TextTypes.TEXT)
        split = split_nodes_delimiter([node], "**", TextTypes.BOLD)
        self.assertEqual(split, [TextNode("Start with bold", TextTypes.BOLD),
                                 TextNode(" text, then go to plain.", TextTypes.TEXT),
                                 ])

    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextTypes.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextTypes.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextTypes.TEXT),
                TextNode("bolded", TextTypes.BOLD),
                TextNode(" word", TextTypes.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextTypes.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextTypes.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextTypes.TEXT),
                TextNode("bolded", TextTypes.BOLD),
                TextNode(" word and ", TextTypes.TEXT),
                TextNode("another", TextTypes.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextTypes.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextTypes.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextTypes.TEXT),
                TextNode("bolded word", TextTypes.BOLD),
                TextNode(" and ", TextTypes.TEXT),
                TextNode("another", TextTypes.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextTypes.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextTypes.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextTypes.TEXT),
                TextNode("italic", TextTypes.ITALIC),
                TextNode(" word", TextTypes.TEXT),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextTypes.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextTypes.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextTypes.TEXT),
                TextNode("code block", TextTypes.CODE),
                TextNode(" word", TextTypes.TEXT),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()