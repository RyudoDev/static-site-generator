from asyncio import ReadTransport

from textnode import TextNode, TextType
from regexes import extract_markdown_links


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes =[]
    for old_node in old_nodes:
        if old_node.text_type == TextType.PLAIN_TEXT:
            old_node_text = old_node.text
            delimiters = extract_markdown_links(old_node_text)
            if len(delimiters) < 1:
                new_nodes.append(old_node)
                continue

            for delimiter in delimiters:
                # Each delimiter is the text/url tuple;
                # the joined one is the reconstruction of the makdown form
                delimiter_joined =  f"[{delimiter[0]}]({delimiter[1]})"
                sections = old_node_text.split(delimiter_joined,1)
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.PLAIN_TEXT, None))
                new_nodes.append(TextNode(delimiter[0],TextType.LINK, delimiter[1]))
                old_node_text = sections[1]
            if old_node_text != "":
                new_nodes.append(TextNode(old_node_text, TextType.PLAIN_TEXT, None))
        else:
            new_nodes.append(old_node)
    return new_nodes
