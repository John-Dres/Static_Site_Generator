from textnode import *
from htmlnode import *

def main():
    #print("Hello World")
    NewTextNode = TextNode("This is a text node",TextType.BOLD,"https://www.boot.dev")
    NewHTMLNode = HTMLNode("<t>", 3, "Child", {"key":"value"})
    NewLeafNode = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(repr(NewTextNode))
    print(repr(NewHTMLNode))
    print(NewLeafNode.to_html())

main()

