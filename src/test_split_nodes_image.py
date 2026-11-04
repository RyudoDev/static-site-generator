from split_nodes_image import split_nodes_image
import unittest
from leafnode import LeafNode
from textnode import TextNode, TextType

class Test_split_nodes_image(unittest.TestCase):

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_image([node])
        theoretical_new_nodes = [
            TextNode("This is text with an ", TextType.PLAIN_TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.PLAIN_TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
        ]
        self.assertListEqual( theoretical_new_nodes,
            new_nodes,
        )

    def test_untouched_plain_block(self):
        node = TextNode("This is text block", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_image([node])
        theoretical_new_nodes = [
            TextNode("This is text block", TextType.PLAIN_TEXT)
        ]
        self.assertEqual(new_nodes, theoretical_new_nodes)


    def test_multiple_blocks(self):
        node_one = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.PLAIN_TEXT)
        node_two = TextNode("This is text with another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_image([node_one, node_two])
        theoretical_new_nodes = [
            TextNode("This is text with an ", TextType.PLAIN_TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode("This is text with another ", TextType.PLAIN_TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
        ]
        self.assertEqual(new_nodes, theoretical_new_nodes)

    def test_duplicate_image(self):
        node_one = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) followed by the same ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_image([node_one])
        theoretical_new_nodes = [
            TextNode("This is text with an ", TextType.PLAIN_TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" followed by the same ", TextType.PLAIN_TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
        ]
        self.assertEqual(new_nodes, theoretical_new_nodes)
