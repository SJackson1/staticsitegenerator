from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(block):
    i = 0
    while block[i] == "#":
        i +=1
        if block[i] == " ":
            return BlockType.HEADING

    if block[0:3] == "```" and block[-3:] == "```":
        return BlockType.CODE

    if block[0] == ">":
        return BlockType.QUOTE

    elif block[0] == "-":
        return BlockType.UNORDERED_LIST
    if block[0].isnumeric() and block[1] == ".":
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH


def markdown_to_blocks(markdown):
    initial_string_list = markdown.split("\n\n")
    final_string_list = []
    for i in range(0,len(initial_string_list)):
        initial_string_list[i] = initial_string_list[i].strip()
        if initial_string_list[i] != "":
            final_string_list.append(initial_string_list[i])
    return final_string_list


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
