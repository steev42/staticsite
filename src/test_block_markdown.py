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


    def test_block_to_type_heading1_match(self):
        text = """# Heading 1"""
        self.assertEqual(BlockTypes.HEADING, block_to_block_type(text))
    
    def test_block_to_type_heading2_match(self):
        text = """## Heading 2"""
        self.assertEqual(BlockTypes.HEADING, block_to_block_type(text))

    def test_block_to_type_heading3_match(self):
        text = """### Heading 3"""
        self.assertEqual(BlockTypes.HEADING, block_to_block_type(text))

    def test_block_to_type_heading4_match(self):
        text = """#### Heading 4"""
        self.assertEqual(BlockTypes.HEADING, block_to_block_type(text))

    def test_block_to_type_heading5_match(self):
        text = """##### Heading 5"""
        self.assertEqual(BlockTypes.HEADING, block_to_block_type(text))

    def test_block_to_type_heading6_match(self):
        text = """###### Heading 6"""
        self.assertEqual(BlockTypes.HEADING, block_to_block_type(text))

    def test_block_to_type_heading7_mismatch(self):
        text = """####### Heading 7"""
        self.assertEqual(BlockTypes.PARAGRAPH, block_to_block_type(text))

    def test_block_to_type_code_match(self):
        text = "```This is a block of code```"
        self.assertEqual(BlockTypes.CODE, block_to_block_type(text))
    
    def test_block_to_type_quote_match(self):
        text = ">This is a quote"
        self.assertEqual(BlockTypes.QUOTE, block_to_block_type(text))

    def test_block_to_type_unordered_match_star(self):
        text = "* One Item List"
        self.assertEqual(BlockTypes.UNORDERED, block_to_block_type(text))

    def test_block_to_type_unordered_match_star_no_space(self):
        text = "*One Item List"
        self.assertEqual(BlockTypes.PARAGRAPH, block_to_block_type(text))

    def test_block_to_type_unordered_match_hyphen(self):
        text = "- One Item List"
        self.assertEqual(BlockTypes.UNORDERED, block_to_block_type(text))
    
    def test_block_to_type_unordered_match_hyphen_no_space(self):
        text = "-One Item List"
        self.assertEqual(BlockTypes.PARAGRAPH, block_to_block_type(text))
    
    def test_block_to_type_ordered_match(self):
        text = "1. One Item Ordered List"
        self.assertEqual(BlockTypes.ORDERED, block_to_block_type(text))
    
    def test_block_to_type_ordered_match_no_space(self):
        text = "1.One Item Ordered List"
        self.assertEqual(BlockTypes.PARAGRAPH, block_to_block_type(text))

    def test_block_to_type_heading_multiline_match(self):
        text = """# Heading 1
More text just to see if it matches"""
        self.assertEqual(BlockTypes.HEADING, block_to_block_type(text))
    
    def test_block_to_type_code_multiline_match(self):
        text = """```Code on one line
continued on another```"""
        self.assertEqual(BlockTypes.CODE, block_to_block_type(text))

    def test_block_to_type_code_no_terminator_mismatch(self):
        text = "```Code without an ending match"
        self.assertEqual(BlockTypes.PARAGRAPH, block_to_block_type(text))

    def test_block_to_type_quote_multiline_match(self):
        text = """>Quote on one line
>Continued on another"""
        self.assertEqual(BlockTypes.QUOTE, block_to_block_type(text))
    
    def test_block_to_type_quote_second_line_no_header(self):
        text = """>Quote on one line
Continued on another"""
        self.assertEqual(BlockTypes.PARAGRAPH, block_to_block_type(text))

    def test_block_to_type_ordered_multiline(self):
        text = """* First object
* Second object"""
        self.assertEqual(BlockTypes.UNORDERED, block_to_block_type(text))
    
    def test_block_to_type_ordered_multiline_hyphen(self):
        text = """- First object
- Second object"""
        self.assertEqual(BlockTypes.UNORDERED, block_to_block_type(text))
    
    def test_block_to_type_ordered_multiline_mixed(self):
        text = """* First object
- Second object"""
        self.assertEqual(BlockTypes.UNORDERED, block_to_block_type(text))

    def test_block_to_type_ordered_multiline_no_space_line_2(self):
        text = """* First object
*Second object"""
        self.assertEqual(BlockTypes.PARAGRAPH, block_to_block_type(text))

    def test_block_to_type_ordered_multiline(self):
        text = """1. First item in ordered list
2. Second item in ordered list
3. Third item in ordered list"""
        self.assertEqual(BlockTypes.ORDERED, block_to_block_type(text))

    def test_block_to_type_ordered_multiline_missing_space(self):
        text = """1. First item in ordered list
2.Second item in ordered list
3. Third item in ordered list"""
        self.assertEqual(BlockTypes.PARAGRAPH, block_to_block_type(text))

    def test_block_to_type_ordered_multiline_not_in_order(self):
        text = """1. First item in ordered list
3. Second item in ordered list
4. Third item in ordered list"""
        self.assertEqual(BlockTypes.PARAGRAPH, block_to_block_type(text))
        
if __name__ == "__main__":
    unittest.main()