import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_without_children(self):
        with self.assertRaises(ValueError) as context:
            parent_node = ParentNode("div", None)
            parent_node.to_html()
        self.assertEqual(str(context.exception), "All parent nodes must have children")

    def test_to_html_without_tag(self):
        with self.assertRaises(ValueError) as context:
            child_node = LeafNode("span", "child")
            parent_node = ParentNode(None, [child_node])
            parent_node.to_html()
        self.assertEqual(str(context.exception), "All parent nodes must have a tag")
    def test_to_html_with_multiple_children(self):
        child_node_a = LeafNode("span", "child_a")
        child_node_b = LeafNode("span", "child_b")
        parent_node = ParentNode("div", [child_node_a, child_node_b],)
        self.assertEqual(parent_node.to_html(), "<div><span>child_a</span><span>child_b</span></div>")

    def test_to_html_with_propped_children(self):
        child_node_a = LeafNode("span", "child_a", {"href": "https://www.google.com"})
        child_node_b = LeafNode("span", "child_b")
        parent_node = ParentNode("div", [child_node_a, child_node_b],)
        self.assertEqual(parent_node.to_html(), '<div><span href="https://www.google.com">child_a</span><span>child_b</span></div>')

    def test_to_html_with_propped_parent(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node],  {"href": "https://www.google.com"})
        self.assertEqual(parent_node.to_html(), '<div href="https://www.google.com"><span>child</span></div>')
