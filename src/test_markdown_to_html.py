import unittest
from markdown_to_html import *

class TestInlineMarkdown(unittest.TestCase):
    def test_paragraph_markdown(self):
        markdown = """Just a simple
multiline paragraph
that should all be contained within
a single paragraph tag."""
        node = markdown_to_paragraph_node(markdown)
        self.assertEqual(node.to_html(), "<p>Just a simple multiline paragraph that should all be contained within a single paragraph tag.</p>")
    
    def test_quote_markdown(self):
        markdown = """>Quoting someone or other
>On multiple lines, of course
>And maybe putting in some **bold** for emphasis?"""
        node = markdown_to_quote_node(markdown)
        self.assertEqual(node.to_html(), "<blockquote>Quoting someone or other On multiple lines, of course And maybe putting in some <b>bold</b> for emphasis?</blockquote>")

    def test_code_markdown(self):
        markdown = """```Some sort of
multiline code block
that needs to be checked```"""
        node = markdown_to_code_node(markdown)
        self.assertEqual(node.to_html(), "<pre><code>Some sort of multiline code block that needs to be checked</code></pre>")

    def test_ordered_markdown(self):
        markdown = """1. First item of business
2. Second item of business
3. Third item has *italics*"""
        node = markdown_to_ordered_list_node(markdown)
        self.assertEqual(node.to_html(), "<ol><li>First item of business</li><li>Second item of business</li><li>Third item has <i>italics</i></li></ol>")
    
    def test_unordered_markdown(self):
        markdown = """* First item of business
* But order doesn't matter
* Third item has *italics*"""
        node = markdown_to_unordered_list_node(markdown)
        self.assertEqual(node.to_html(), "<ul><li>First item of business</li><li>But order doesn't matter</li><li>Third item has <i>italics</i></li></ul>")
    
    def test_header_markdown(self):
        markdown = """# Header 1
somehow has multiple lines, but
that should still be ok!"""
        node = markdown_to_header_node(markdown)
        self.assertEqual(node.to_html(), "<h1>Header 1 somehow has multiple lines, but that should still be ok!</h1>")

    def test_header_markdown3(self):
        markdown = """### Header 3
just in case."""
        node = markdown_to_header_node(markdown)
        self.assertEqual(node.to_html(), "<h3>Header 3 just in case.</h3>")

    def test_all_together(self):
        markdown = """# Markdown header

>This is a quote for posterity
>and it is split on to multiple lines.

## Second section

* Unordered
* Lists
* Need
* To
* Work

### Third Section

1. So
2. Do
3. Ordered
4. Lists

#### Fourth Section

```Put a bit of code block
in here just for luck.```

##### Fifth Section

Just a blank paragraph here.  We'll put in some **Bold Text**
and some *Italic Text* for sure, and maybe even put in an
![image](image.png) and maybe, just maybe a [link](link.html)

###### Sixth Section

About the only thing we haven't hit at this point is
some `inline code sections`, so we'll put that here. 

And just for completeness, we'll check that no h7 exists

####### Seventh Section? Hopefully not!

Did that work?"""
        
        node = markdown_to_html_node(markdown)
        expected_result = "<div>"
        expected_result += "<h1>Markdown header</h1>"
        expected_result += "<blockquote>This is a quote for posterity and it is split on to multiple lines.</blockquote>"
        expected_result += "<h2>Second section</h2>"
        expected_result += "<ul><li>Unordered</li><li>Lists</li><li>Need</li><li>To</li><li>Work</li></ul>"
        expected_result += "<h3>Third Section</h3>"
        expected_result += "<ol><li>So</li><li>Do</li><li>Ordered</li><li>Lists</li></ol>"
        expected_result += "<h4>Fourth Section</h4>"
        expected_result += "<pre><code>Put a bit of code block in here just for luck.</code></pre>"
        expected_result += "<h5>Fifth Section</h5>"
        expected_result += "<p>Just a blank paragraph here.  We'll put in some <b>Bold Text</b> and some <i>Italic Text</i> for sure, and maybe even put in an "
        expected_result += '<img src="image.png" alt="image"></img> and maybe, just maybe a <a href="link.html">link</a></p>'
        expected_result += "<h6>Sixth Section</h6>"
        expected_result += "<p>About the only thing we haven't hit at this point is some <code>inline code sections</code>, so we'll put that here.</p>"
        expected_result += "<p>And just for completeness, we'll check that no h7 exists</p>"
        expected_result += "<p>####### Seventh Section? Hopefully not!</p>"
        expected_result += "<p>Did that work?</p>"
        expected_result += "</div>"

        self.maxDiff = None
        self.assertEqual(node.to_html(), expected_result)



if __name__ == "__main__":
    unittest.main()