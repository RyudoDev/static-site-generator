from __future__ import annotations
from typing import override
from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    # By definition it has no children, and requires tag and vlaue, although the tag can be None
    def __init__(self, tag: str | None,
                 children: list[HTMLNode] | None,
                 props: dict[str, str] | None = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag")
        if self.children is None:
            raise ValueError("All parent nodes must have children")
        html = f"<{self.tag}"
        if self.props is not None:
            html += self.props_to_html()
        html += ">"
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"
        return html
