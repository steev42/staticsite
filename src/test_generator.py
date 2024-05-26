import unittest
from generator import *

class TestGenerator(unittest.TestCase):
    
    def test_extract_title_works(self):
        markdown = """# Header 1 

And an extra paragraph."""
        title = extract_title(markdown)
        self.assertEqual(title, "Header 1")

    
    def test_extract_title_exception(self):
        markdown= """This is a paragraph
        
This markdown has no header
        
I expect an exception!"""
        with self.assertRaises(Exception):
            extract_title(markdown)

if __name__ == "__main__":
    unittest.main()