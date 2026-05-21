from textnode import TextType,TextNode
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
