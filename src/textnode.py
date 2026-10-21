from __future__ import annotations
from enum import Enum
from leafnode import LeafNode



class TextType(Enum):
    PLAIN_TEXT = "plain"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: TextNode):
        return self.text == other.text and self.text_type.value == other.text_type.value and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node: TextNode) -> LeafNode:

    match text_node.text_type:
        case TextType.PLAIN_TEXT:
            return LeafNode(None, text_node.text, None)
        case TextType.BOLD_TEXT:
            return LeafNode("b", text_node.text, None)

        case TextType.ITALIC_TEXT:
            return LeafNode("i", text_node.text, None)

        case TextType.CODE_TEXT:
            return LeafNode("code", text_node.text, None)

        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})

        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

        case _:
            raise ValueError(f"Invalid text type: {text_node.text_type}")
