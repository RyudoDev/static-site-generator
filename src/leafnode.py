from __future__ import annotations
from typing import override
from htmlnode import HTMLNode

class LeafNode(HTMLNode):

    # By definition it has no children, and requires tag and vlaue, although the tag can be None
    def __init__(self, tag: str | None,
                 value: str | None,
                 props: dict[str, str] | None = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        to_print = ""
        to_print += f"tag: {self.tag}\n"
        to_print += f"value: {self.value}\n"
        if self.props is None:
            to_print += "no props\n"
        else:
            to_print += "props:\n"
            for key, value in self.props.items():
                to_print += f"    -key: {key}, value: {value}\n"
        return to_print
