from textnode import *
from htmlnode import *
from myfunctions import *

def main():
    #print("Hello World")
    NewTextNode = TextNode("This is a text node",TextType.BOLD,"https://www.boot.dev")
    NewHTMLNode = HTMLNode("<t>", 3, "Child", {"key":"value"})
    NewLeafNode = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    Leaf1 = LeafNode("b", "Bold text")
    Leaf2 = LeafNode(None, "Normal text")
    Leaf3 = LeafNode("i", "italic text")
    Leaf4 = LeafNode(None, "Normal text")
    NewParentNode = ParentNode("p", [Leaf1, Leaf2, Leaf3, Leaf4])
    FunctionTest = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
    text_image = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    text_link = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(f"Print 1: {repr(NewTextNode)}")
    print(f"Print 2: {repr(NewHTMLNode)}")
    print(f"Print 3: {NewLeafNode.to_html()}")
    print(f"Print 4: {NewParentNode.to_html()}")
    print(f"Print 5: {split_nodes_delimiter([FunctionTest], "**", TextType.BOLD)}")
    print(f"Print 6: {extract_markdown_images(text_image)}")
    print(f"Print 7: {extract_markdown_links(text_link)}")


    node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,)
    print(f"Print 8: {extract_markdown_links(node.text)}")
    matches = extract_markdown_links(node.text)
    print(f"Print 9: {matches}")
    #print(f"Print 10: {split_nodes_link([node])}")
    #node2 = TextNode("Hello [link1](url1) middle [link2](url2) end", TextType.TEXT)
    #print(f"Print 11: {split_nodes_link([node2])}")
    #node3 = TextNode("[link1](url1)some text[link2](url2)", TextType.TEXT)
    #print(f"Print 12: {split_nodes_link([node3])}")
    node1 = TextNode("![alt](url)more text", TextType.TEXT)
    node2 = TextNode("text![alt](url)", TextType.TEXT)
    node3 = TextNode("![alt1](url1)![alt2](url2)", TextType.TEXT)
    node4 = TextNode("Just plain text", TextType.TEXT)
    print(f"Node 1: {split_nodes_image([node1])}")
    print(f"Node 2: {split_nodes_image([node2])}")
    print(f"Node 3: {split_nodes_image([node3])}")
    print(f"Node 4: {split_nodes_image([node4])}")

main()

