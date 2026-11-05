from textnode import TextNode, TextType
from htmlnode import HTMLNode
from split_nodes_image import split_nodes_image

def main():
    node = TextNode("![image](https://i.imgur.com/zjjcJKZ.png) is at the start", TextType.PLAIN_TEXT)
    new_nodes = split_nodes_image([node])
    print(new_nodes)
main()
