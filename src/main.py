from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    child1 = HTMLNode("li", "Item One", None, None)
    child2_1 = HTMLNode("li", "Item One", None, None)
    child2 = HTMLNode("li", "Item One", [child2_1], None)
    parent = HTMLNode("ul", None, [child1, child2], None)
    print(parent)
main()
