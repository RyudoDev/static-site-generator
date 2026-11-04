from asyncio import ReadTransport

from textnode import TextNode, TextType
from regexes import extract_markdown_images


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes =[]
    for old_node in old_nodes:
        if old_node.text_type == TextType.PLAIN_TEXT:
            old_node_text = old_node.text
            delimiters = extract_markdown_images(old_node_text)
            if len(delimiters) < 1:
                new_nodes.append(old_node)
                continue

            for delimiter in delimiters:
                # Each delimiter is the text/url tuple;
                # the joined one is the reconstruction of the makdown form
                delimiter_joined =  f"![{delimiter[0]}]({delimiter[1]})"
                sections = old_node_text.split(delimiter_joined,1)
                new_nodes.append(TextNode(sections[0], TextType.PLAIN_TEXT, None))
                new_nodes.append(TextNode(delimiter[0],TextType.IMAGE, delimiter[1]))
                old_node_text = sections[1]
        else:
            new_nodes.append(old_node)
    return new_nodes

def split_nodes_image_helper(new_nodes, old_node, delimiters):
    if len(delimiters) == 1:
        delimiter_joined =  f"![{delimiter[0]}]({delimiter[1]})"
        sections = old_node.text.split(delimiter_joined)
        for index in range(len(sections)):
            section = sections[index]
            if index > 0:
                #This way it intercalates the text sections with the images.
                # It is done in a loop since the same image could be in the same block more than once.
                new_nodes.append(TextNode(delimiter[0],TextType.IMAGE, delimiter[1]))
            if section != "":
                new_nodes.append(TextNode(section, TextType.PLAIN_TEXT, None))
