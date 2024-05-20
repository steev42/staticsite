import unittest

from textnode import (
    TextNode,
    TextTypes
    )

from block_markdown import *

class TestInlineMarkdown(unittest.TestCase):
    def test_markdown_split(self):
        text = """This is **bolded** paragraph

                This is another paragraph with *italic* text and `code` here
                This is the same paragraph on a new line

                * This is a list
                * with items"""

        split = markdown_to_blocks(text)
        
#        print (split)
        self.assertEqual(split, [
"This is **bolded** paragraph",
"""This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line""",
"""* This is a list
* with items"""
                        ])

    def test_markdown_split_empty(self):
        text = ""
        split = markdown_to_blocks(text)
        self.assertEqual(split, [])

    def test_markdown_split_extra_lines(self):
        text = """This is **bolded** paragraph

        

                This is another paragraph with *italic* text and `code` here
                This is the same paragraph on a new line

                
                
                * This is a list
                * with items"""

        split = markdown_to_blocks(text)
        
#        print (split)
        self.assertEqual(split, [
"This is **bolded** paragraph",
"""This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line""",
"""* This is a list
* with items"""
                        ])


if __name__ == "__main__":
    unittest.main()