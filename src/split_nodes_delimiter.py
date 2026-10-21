from asyncio import ReadTransport

from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes =[]
    for old_node in old_nodes:
        if old_node.text_type == TextType.PLAIN_TEXT and delimiter in old_node.text:
            sections = old_node.text.split(delimiter)
            # Odd means unmatched opener
            if len(sections) % 2 == 0:
                raise Exception(f"Invalid Markdown syntax: Unmatched opening '{delimiter}' delimiter")
            for index in range(len(sections)):
                section = sections[index]
                match index % 2:
                    case 0:
                        new_node = TextNode(section, TextType.PLAIN_TEXT)

                    case 1:
                        new_node = TextNode(section, text_type)
                new_nodes.append(new_node)
        else:
            new_nodes.append(old_node)
    return new_nodes
