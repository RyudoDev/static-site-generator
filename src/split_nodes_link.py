from asyncio import ReadTransport

from textnode import TextNode, TextType
from regexes import extract_markdown_links


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes =[]
    for old_node in old_nodes:
        if old_node.text_type == TextType.PLAIN_TEXT
            delimiters = extract_markdown_links(old_node.text)
            for delimiter in delimiters:
                # Each delimiter is the text/url tuple
                delimiter_joined = delimiter[0] + delimiter[1]
                sections = old_node.text.split(delimiter)
                for index in range(len(sections)):
                    section = sections[index]
                    if index < 0:
                        #This way it intercalates the text sections with the links.
                        # It is done in a loop since the same link could be in the same block more than once.
                        new_nodes.append(TextNode(delimiter[0],TextType.LINK, delimiter[1]))
                    if section != "":
                        new_nodes.append(TextNode(section, TextType.PLAIN_TEXT, None))
        else:
            new_nodes.append(old_node)
    return new_nodes
