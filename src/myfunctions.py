from textnode import *
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    if len(old_nodes) == 0:
        raise ValueError("Empty list")
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
        else:
            split_text = old_node.text.split(delimiter)
            if len(split_text)%2 == 0:
                raise SyntaxError(f"Invalid Markdown syntax in node: '{old_node.text}'")
            new_text_nodes = []
            for i in range(len(split_text)):
                if split_text[i] == "":
                    continue
                elif i%2 == 0:
                    new_node = TextNode(split_text[i], TextType.TEXT)
                else:
                    new_node = TextNode(split_text[i], text_type)
                new_text_nodes.append(new_node)
            new_nodes.extend(new_text_nodes)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
   
def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        matches = extract_markdown_images(old_node.text)
        if old_node.text is None:
            continue
        elif matches == []:
            new_nodes.append(old_node)
        else:
            remaining_text = old_node.text   
            for match in matches:
                image_alt = match[0]
                image_link = match[1]
                section = remaining_text.split(f"![{image_alt}]({image_link})", 1)
                if section[0] != "":
                    new_Textnode = TextNode(section[0], TextType.TEXT)
                    new_nodes.append(new_Textnode)
                new_Image_Textnode = TextNode(image_alt, TextType.IMAGE, image_link)
                new_nodes.append(new_Image_Textnode)
                remaining_text = section[1]
            if remaining_text != "":
                final_Textnode = TextNode(remaining_text, TextType.TEXT)
                new_nodes.append(final_Textnode)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        matches = extract_markdown_links(old_node.text)
        if old_node.text is None:
            continue
        elif matches == []:
            new_nodes.append(old_node)
        else:
            remaining_text = old_node.text   
            for match in matches:
                link_alt = match[0]
                link_url = match[1]
                section = remaining_text.split(f"[{link_alt}]({link_url})", 1)
                if section[0] != "":
                    new_Textnode = TextNode(section[0], TextType.TEXT)
                    new_nodes.append(new_Textnode)
                new_Link_Textnode = TextNode(link_alt, TextType.LINK, link_url)
                new_nodes.append(new_Link_Textnode)
                remaining_text = section[1]
            if remaining_text != "":
                final_Textnode = TextNode(remaining_text, TextType.TEXT)
                new_nodes.append(final_Textnode)
    return new_nodes

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    bold = split_nodes_delimiter([node], "**", TextType.BOLD)
    italic = split_nodes_delimiter(bold, "*", TextType.ITALIC)
    code = split_nodes_delimiter(italic, "`", TextType.CODE)
    image = split_nodes_image(code)
    link = split_nodes_link(image)
    return link