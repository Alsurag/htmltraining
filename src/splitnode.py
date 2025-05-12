from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_one in old_nodes:
        if old_one.text_type != TextType.TEXT:
            new_nodes.append(old_one)
            continue

        text = old_one.text
        start_index = text.find(delimiter)

        if start_index == -1:
            new_nodes.append(old_one)
            continue

        end_index = text.find(delimiter, start_index + len(delimiter))

        if end_index == -1:
            raise Exception(f"No closing delimiter {delimiter} found")
        
        before_text = text[:start_index]
        delimited_text = text[start_index + len(delimiter):end_index]
        after_text = text[end_index + len(delimiter):]

        if before_text:
            new_nodes.append(TextNode(before_text, TextType.TEXT))
        
        new_nodes.append(TextNode(delimited_text, text_type))

        if after_text:
            remaining_node = TextNode(after_text, TextType.TEXT)
            new_nodes.extend(split_nodes_delimiter([remaining_node], delimiter, text_type))

    return new_nodes