from split_nodes_link import split_nodes_link
import unittest
from leafnode import LeafNode
from textnode import TextNode, TextType

class Test_split_nodes_link(unittest.TestCase):

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://www.google.com) and another [second link](https://www.boot.dev)",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_link([node])
        theoretical_new_nodes = [
            TextNode("This is text with a ", TextType.PLAIN_TEXT),
            TextNode("link", TextType.LINK, "https://www.google.com"),
            TextNode(" and another ", TextType.PLAIN_TEXT),
            TextNode("second link", TextType.LINK, "https://www.boot.dev"),
        ]
        self.assertListEqual( theoretical_new_nodes,
            new_nodes,
        )

    def test_untouched_plain_block(self):
        node = TextNode("This is text block", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_link([node])
        theoretical_new_nodes = [
            TextNode("This is text block", TextType.PLAIN_TEXT)
        ]
        self.assertEqual(new_nodes, theoretical_new_nodes)


    def test_multiple_blocks(self):
        node_one = TextNode("This is text with a [link](https://www.google.com)", TextType.PLAIN_TEXT)
        node_two = TextNode("This is text with another [second link](https://www.boot.dev)", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_link([node_one, node_two])
        theoretical_new_nodes = [
            TextNode("This is text with a ", TextType.PLAIN_TEXT),
            TextNode("link", TextType.LINK, "https://www.google.com"),
            TextNode("This is text with another ", TextType.PLAIN_TEXT),
            TextNode("second link", TextType.LINK, "https://www.boot.dev"),
        ]
        self.assertEqual(new_nodes, theoretical_new_nodes)

    def test_duplicate_link(self):
        node_one = TextNode("This is text with a [link](https://www.google.com) followed by the same [link](https://www.google.com)", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_link([node_one])
        theoretical_new_nodes = [
            TextNode("This is text with a ", TextType.PLAIN_TEXT),
            TextNode("link", TextType.LINK, "https://www.google.com"),
            TextNode(" followed by the same ", TextType.PLAIN_TEXT),
            TextNode("link", TextType.LINK, "https://www.google.com"),
        ]
        self.assertEqual(new_nodes, theoretical_new_nodes)

    def test_emtpy_string(self):
        node_one = TextNode("", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_link([node_one])
        self.assertEqual(new_nodes, [node_one])

    def test_link_at_start(self):
        node = TextNode("[link](https://www.google.com) is at the start", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_link([node])
        theoretical_new_nodes = [
            TextNode("link", TextType.LINK,"https://www.google.com"),
            TextNode(" is at the start", TextType.PLAIN_TEXT),
        ]
        self.assertEqual(theoretical_new_nodes, new_nodes)

    def test_image_and_link(self):
        node = TextNode(
            "This is text with a [link](https://www.google.com) and an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_link([node])
        theoretical_new_nodes = [
            TextNode("This is text with a ", TextType.PLAIN_TEXT),
            TextNode("link", TextType.LINK, "https://www.google.com"),
            TextNode(" and an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.PLAIN_TEXT),
        ]
        self.assertListEqual( theoretical_new_nodes,
            new_nodes,
        )
