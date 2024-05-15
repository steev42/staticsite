import unittest

from textnode import (
    TextNode,
    TextTypes
    )

from inline_markdown import *

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
    
    def test_image_extraction(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        tuple = extract_markdown_images(text)
        self.assertListEqual(
            [
            ('image','https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png'),
            ('another', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png')
            ],
            tuple
        )
    
    def test_image_extraction_no_image_found(self):
        text = "This is an example text with absolutely no inline images to be found!"
        tuple = extract_markdown_images(text)
        self.assertListEqual(
            [],
            tuple
        )

    def test_link_extraction(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        tuple = extract_markdown_links(text)
        self.assertListEqual(
            [
            ('link','https://www.example.com'),
            ('another', 'https://www.example.com/another')
            ],
            tuple
        )

    def test_link_extraction_no_image_found(self):
        text = "This is an example text with absolutely no inline links to be found!"
        tuple = extract_markdown_images(text)
        self.assertListEqual(
            [],
            tuple
        )

    def test_image_delim_single(self):
        node = TextNode("This is a text with a ![image](image.jpg) single image to deliminate.", TextTypes.TEXT)
        list = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is a text with a ", TextTypes.TEXT),
                TextNode("image", TextTypes.IMAGE, "image.jpg"),
                TextNode(" single image to deliminate.", TextTypes.TEXT)
            ],
            list
        )
    
    def test_image_delim_at_end(self):
        node = TextNode("This is a text with the image at the end ![image](image.jpg)", TextTypes.TEXT)
        list = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is a text with the image at the end ", TextTypes.TEXT),
                TextNode("image", TextTypes.IMAGE, "image.jpg")
            ],
            list
        )
    
    def test_image_delim_multiple(self):
        node = TextNode("This is a text with ![image](image.jpg) more than a ![another](img.jpg) single image to deliminate.", TextTypes.TEXT)
        list = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is a text with ", TextTypes.TEXT),
                TextNode("image", TextTypes.IMAGE, "image.jpg"),
                TextNode(" more than a ", TextTypes.TEXT),
                TextNode("another", TextTypes.IMAGE, "img.jpg"),
                TextNode(" single image to deliminate.", TextTypes.TEXT)
            ],
            list
        )

    def test_image_delim_none(self):
        node = TextNode("This is a text without images to deliminate", TextTypes.TEXT)
        list = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is a text without images to deliminate", TextTypes.TEXT)
            ],
            list
        )

    def test_image_delim_multiple_nodes(self):
        node1 = TextNode("This is a text with a ![image](image.jpg) single image to deliminate.", TextTypes.TEXT)
        node2 = TextNode("This is another text with a ![another](img.png) single image to deliminate.", TextTypes.TEXT)
        
        list = split_nodes_image([node1, node2])
        self.assertListEqual(
            [
                TextNode("This is a text with a ", TextTypes.TEXT),
                TextNode("image", TextTypes.IMAGE, "image.jpg"),
                TextNode(" single image to deliminate.", TextTypes.TEXT),
                TextNode("This is another text with a ", TextTypes.TEXT),
                TextNode("another", TextTypes.IMAGE, "img.png"),
                TextNode(" single image to deliminate.", TextTypes.TEXT)
            ],
            list
        )

    def test_link_delim_single(self):
        node = TextNode("This is a text with a [alt](http://boot.dev) single link to deliminate.", TextTypes.TEXT)
        list = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a text with a ", TextTypes.TEXT),
                TextNode("alt", TextTypes.LINK, "http://boot.dev"),
                TextNode(" single link to deliminate.", TextTypes.TEXT)
            ],
            list
        )
    
    def test_link_delim_at_end(self):
        node = TextNode("This is a text with the link at the end [alt](http://boot.dev)", TextTypes.TEXT)
        list = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a text with the link at the end ", TextTypes.TEXT),
                TextNode("alt", TextTypes.LINK, "http://boot.dev")
            ],
            list
        )
    
    def test_link_delim_multiple(self):
        node = TextNode("This is a text with [alt](http://boot.dev) more than a [another](http://google.com) single link to deliminate.", TextTypes.TEXT)
        list = split_nodes_link([node])
        #print(list)
        self.assertListEqual(
            [
                TextNode("This is a text with ", TextTypes.TEXT),
                TextNode("alt", TextTypes.LINK, "http://boot.dev"),
                TextNode(" more than a ", TextTypes.TEXT),
                TextNode("another", TextTypes.LINK, "http://google.com"),
                TextNode(" single link to deliminate.", TextTypes.TEXT)
            ],
            list
        )

    def test_link_delim_none(self):
        node = TextNode("This is a text without links to deliminate", TextTypes.TEXT)
        list = split_nodes_link([node])
        #print(list)
        self.assertListEqual(
            [
                TextNode("This is a text without links to deliminate", TextTypes.TEXT)
            ],
            list
        )
    
    def test_link_delim_multiple_nodes(self):
        node1 = TextNode("This is a text with a [alt](http://boot.dev) single link to deliminate.", TextTypes.TEXT)
        node2 = TextNode("This is another text with a [morealt](http://google.com) single link to deliminate.", TextTypes.TEXT)
        list = split_nodes_link([node1, node2])
        self.assertListEqual(
            [
                TextNode("This is a text with a ", TextTypes.TEXT),
                TextNode("alt", TextTypes.LINK, "http://boot.dev"),
                TextNode(" single link to deliminate.", TextTypes.TEXT),
                TextNode("This is another text with a ", TextTypes.TEXT),
                TextNode("morealt", TextTypes.LINK, "http://google.com"),
                TextNode(" single link to deliminate.", TextTypes.TEXT)
            ],
            list
        )
    
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        expected_result = [
            TextNode("This is ", TextTypes.TEXT),
            TextNode("text", TextTypes.BOLD),
            TextNode(" with an ", TextTypes.TEXT),
            TextNode("italic", TextTypes.ITALIC),
            TextNode(" word and a ", TextTypes.TEXT),
            TextNode("code block", TextTypes.CODE),
            TextNode(" and an ", TextTypes.TEXT),
            TextNode("image", TextTypes.IMAGE, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and a ", TextTypes.TEXT),
            TextNode("link", TextTypes.LINK, "https://boot.dev")
            ]
    
        self.assertListEqual(nodes, expected_result)

if __name__ == "__main__":
    unittest.main()