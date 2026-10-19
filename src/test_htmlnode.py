import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("img",  None , None, {
            "src": "cat.png",
            "alt": "A cat",
            "width": "200",
        })
        self.assertEqual(node.props_to_html(), ' src="cat.png" alt="A cat" width="200"')

    def test_props_to_html_no_props(self):
        node = HTMLNode("img",  None , None, None)
        self.assertEqual(node.props_to_html(), "")

    def test_to_html_error(self):
        with self.assertRaises(NotImplementedError) as context:
            node = HTMLNode()
            node.to_html()

if __name__ == "__main__":
    unittest.main()
