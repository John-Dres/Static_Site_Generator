from textnode import *
from htmlnode import *

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
    print(f"Print 1: {repr(NewTextNode)}")
    print(f"Print 2: {repr(NewHTMLNode)}")
    print(f"Print 3: {NewLeafNode.to_html()}")
    print(f"Print 4: {NewParentNode.to_html()}")

main()

