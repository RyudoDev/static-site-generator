import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_no_value_error(self):
        with self.assertRaises(ValueError) as context:
            node = LeafNode(None, None)
            node.to_html()

    def test_no_props_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_props_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_tagless(self):
        node = LeafNode(None, "This is tagless text.")
        self.assertEqual(node.to_html(), "This is tagless text.")
