import unittest
from blocks import markdown_to_blocks, block_to_block_type, BlockType

class TestHTMLNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
           md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
   """
           blocks = markdown_to_blocks(md)
           self.assertEqual(
               blocks,
               [
                   "This is **bolded** paragraph",
                   "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                   "- This is a list\n- with items",
               ],
           )

    def test_block_to_block_type_para(self):
        block = "Just a normal paragraph"
        self.assertEqual(block_to_block_type(block),BlockType.PARAGRAPH)

    def test_block_to_block_type_heading(self):
        block = "### Just a normal heading"
        self.assertEqual(block_to_block_type(block),BlockType.HEADING)

    def test_block_to_block_type_code(self):
        block = "```Just normal code ```"
        self.assertEqual(block_to_block_type(block),BlockType.CODE)

    def test_block_to_block_type_quote(self):
        block  = ">random quote"
        self.assertEqual(block_to_block_type(block),BlockType.QUOTE)

    def test_block_to_block_type_unordered(self):
        block  = "- something unordered"
        self.assertEqual(block_to_block_type(block),BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ordered(self):
        block  = "1. something ordered"
        self.assertEqual(block_to_block_type(block),BlockType.ORDERED_LIST)
