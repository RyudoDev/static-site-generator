from __future__ import annotations
from typing import override

class HTMLNode:
    # if tag is none, it's plain text. if it doesn't have value, it has children. If it has no chidren, it has value. If it has no props, it has no attributes.
    def __init__(self, tag: str | None = None,
                 value: str | None = None,
                 children: list[HTMLNode] | None = None,
                 props: dict[str, str] | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html = ""
        if self.props is not None:
            for prop, value in self.props.items():
                prop_text = f' {prop}="{value}"'
                html += prop_text
        return html

    def __repr__(self) -> str:
        to_print = ""
        to_print += f"tag: {self.tag}\n"
        to_print += f"value: {self.value}\n"
        if self.children is None:
            to_print += "no children\n"
        else:
            to_print += "children:\n"
            for child in self.children:
                to_print += "---child start---\n"
                to_print += f"{child}"
                to_print += "---child end  ---\n"

        if self.props is None:
            to_print += "no props\n"
        else:
            to_print += "props:\n"
            for key, value in self.props.items():
                to_print += f"    -key: {key}, value: {value}\n"
        return to_print
