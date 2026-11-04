from split_nodes_link import split_nodes_link
import unittest
from leafnode import LeafNode
from textnode import TextNode, TextType

class Test_split_nodes_delimiter(unittest.TestCase):



    def test_bold_block(self):
        node = TextNode("This is text with a **bold** word", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        theoretical_new_nodes = [
            TextNode("This is text with a ", TextType.PLAIN_TEXT),
            TextNode("bold", TextType.BOLD_TEXT),
            TextNode(" word", TextType.PLAIN_TEXT),
        ]
        self.assertEqual(new_nodes, theoretical_new_nodes)

    def test_italic_block(self):
        node = TextNode("This is text with an _italic_ word", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)
        theoretical_new_nodes = [
            TextNode("This is text with an ", TextType.PLAIN_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" word", TextType.PLAIN_TEXT),
        ]
        self.assertEqual(new_nodes, theoretical_new_nodes)

    def test_multiple_segment_block(self):
        node = TextNode("This is text with a _first italic text segment_ and a _second one_", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)
        theoretical_new_nodes = [
            TextNode("This is text with a ", TextType.PLAIN_TEXT),
            TextNode("first italic text segment", TextType.ITALIC_TEXT),
            TextNode(" and a ", TextType.PLAIN_TEXT),
            TextNode("second one", TextType.ITALIC_TEXT)
        ]
        self.assertEqual(new_nodes, theoretical_new_nodes)

    def test_incomplete_block(self):
        with self.assertRaises(Exception) as context:
            node = TextNode("This is text with an incomplete _italic block", TextType.PLAIN_TEXT)
            new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)
        self.assertEqual(str(context.exception), "Invalid Markdown syntax: Unmatched opening '_' delimiter")

    def test_untouched_plain_block(self):
        node = TextNode("This is text block", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)
        theoretical_new_nodes = [
            TextNode("This is text block", TextType.PLAIN_TEXT)
        ]
        self.assertEqual(new_nodes, theoretical_new_nodes)

    def test_untouched_bold_block(self):
        node = TextNode("**This is bold text block**", TextType.BOLD_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        theoretical_new_nodes = [
            TextNode("**This is bold text block**", TextType.BOLD_TEXT)
        ]
        self.assertEqual(new_nodes, theoretical_new_nodes)

    def test_all_bold_block(self):
        node = TextNode("**This is bold text block**", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        theoretical_new_nodes = [
            TextNode("This is bold text block", TextType.BOLD_TEXT)
        ]
        self.assertEqual(new_nodes, theoretical_new_nodes)

    def test_multiple_blocks(self):
        node_one = TextNode("This is text with an _italic_ word", TextType.PLAIN_TEXT)
        node_two = TextNode("This is text with a **bold** word", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node_one, node_two], "_", TextType.ITALIC_TEXT)
        theoretical_new_nodes = [
            TextNode("This is text with an ", TextType.PLAIN_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" word", TextType.PLAIN_TEXT),
            TextNode("This is text with a **bold** word", TextType.PLAIN_TEXT)
        ]
        self.assertEqual(new_nodes, theoretical_new_nodes)
