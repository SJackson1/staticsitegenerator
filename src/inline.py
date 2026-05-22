from textnode import TextType,TextNode
import re
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    text_node_list = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.PLAIN:
            text_node_list.append(old_node)
        else:
            split_node_list = old_node.text.split(delimiter)
            if len(split_node_list)%2 == 0:
                raise Exception("invalid markdown syntax")
            else:
                for i in range(1,len(split_node_list)+1):
                    if i % 2 == 1 and split_node_list[i-1] != "":
                        text_node_list.append(TextNode(split_node_list[i-1],TextType.PLAIN))
                    elif i % 2 == 0 and split_node_list[i-1] != "":
                        text_node_list.append(TextNode(split_node_list[i-1],text_type))
    return text_node_list

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)

def split_nodes_image(old_nodes):
    text_node_list = []
    for old_node in old_nodes:
        extracted = extract_markdown_images(old_node.text)
        if len(extracted) == 0:
            text_node_list.append(old_node)
        else:
            sections = old_node.text.split(f"![{extracted[0][0]}]({extracted[0][1]})", 1)
            if len(extracted) == 1:
                if sections[0] != "":
                    text_node_list.append(TextNode(sections[0],TextType.PLAIN))
                text_node_list.append(TextNode(extracted[0][0],TextType.IMAGES,extracted[0][1]))
            elif len(extracted) > 1:
                if sections[0] != "":
                    text_node_list.append(TextNode(sections[0],TextType.PLAIN))
                text_node_list.append(TextNode(extracted[0][0],TextType.IMAGES,extracted[0][1]))
                for i in range(1,len(extracted)):
                    sections = sections[1].split(f"![{extracted[i][0]}]({extracted[i][1]})", 1)
                    if sections[0] != "":
                        text_node_list.append(TextNode(sections[0],TextType.PLAIN))
                    text_node_list.append(TextNode(extracted[i][0],TextType.IMAGES,extracted[i][1]))

    return text_node_list

def split_nodes_link(old_nodes):
    text_node_list = []
    for old_node in old_nodes:
        extracted = extract_markdown_links(old_node.text)
        if len(extracted) == 0:
            text_node_list.append(old_node)
        else:
            sections = old_node.text.split(f"[{extracted[0][0]}]({extracted[0][1]})", 1)
            if len(extracted) == 1:
                if sections[0] != "":
                    text_node_list.append(TextNode(sections[0],TextType.PLAIN))
                text_node_list.append(TextNode(extracted[0][0],TextType.LINKS,extracted[0][1]))
            elif len(extracted) > 1:
                if sections[0] != "":
                    text_node_list.append(TextNode(sections[0],TextType.PLAIN))
                text_node_list.append(TextNode(extracted[0][0],TextType.LINKS,extracted[0][1]))
                for i in range(1,len(extracted)):
                    sections = sections[1].split(f"[{extracted[i][0]}]({extracted[i][1]})", 1)
                    if sections[0] != "":
                        text_node_list.append(TextNode(sections[0],TextType.PLAIN))
                    text_node_list.append(TextNode(extracted[i][0],TextType.LINKS,extracted[i][1]))

    return text_node_list


def text_to_textnodes(text):
    nodes = [TextNode(text,TextType.PLAIN)]
    nodes = split_nodes_delimiter(nodes,"**",TextType.BOLD)
    nodes = split_nodes_delimiter(nodes,"_",TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes,"`",TextType.CODE)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    return nodes
