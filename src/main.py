from textnode import *
from htmlnode import *
from myfunctions import *
from block_markdown import *

def main():
    """print("Hello World")
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
    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    ConvertTest = TextNode(text, TextType.TEXT)
    print(f"Convert Test: {split_nodes_delimiter([ConvertTest], "**", TextType.BOLD)}")
    BoldTextNodeObjects = split_nodes_delimiter([ConvertTest], "**", TextType.BOLD)
    print(f"Convert Test2: {split_nodes_delimiter(BoldTextNodeObjects, "*", TextType.ITALIC)}")
    print(f"Function Test: {text_to_textnodes(text)}")
    markdown_test = "  # First Block  \n\nSecond Block\n\n\n\n\nThird Block\nAlso Third Block"
    print(f"Markdown Test: {markdown_test}")
    print(f"Markdown_To_Blocks_Test: {markdown_to_blocks(markdown_test)}")
    print(f"Splitlines Test: {markdown_test.splitlines()}")
    test_string = '##### heading 2'
    partition = test_string.partition(' ')
    print(f"Remove Prefix Test: {partition[2]}")
    quote_test = '> First line\n> Second Line\n> Third line'
    quote_lines = quote_test.splitlines()
    final_quote = ''
    for quote_line in quote_lines:
        partition = quote_line.partition(' ')
        final_quote += f" {partition[2]}
    for quote_line in quote_lines:
        final_quote += f" {quote_line.removeprefix('> ')}"
    print(f"Quote Test: {final_quote.strip()}")
    #print(f"Quote Test: {final_quote}")
    QuoteNode = quote_to_htmlnode(quote_test)
    print(f"Quote Node: {QuoteNode}")
    code = '```\nThis is code\n\nThis still is\n```'
    print(f"Code:\n{code.strip("`\n")}")
    code = "```\nThis is text that _should_ remain the **same** even with inline stuff\n```"
    full_code = code.strip("`\n`")
    CodeTextNode = TextNode(full_code, TextType.CODE)
    CodeLeafNode = CodeTextNode.text_node_to_html_node()
    PreNode = ParentNode("pre", CodeLeafNode)
    print(f"Test: {PreNode}")"""
    #text = "**bold Heading** normal text"
    #heading = "# Heading 1 with **bold text**\n## Heading 2 with *italic text*\n### Heading 3 with ```code text```"
    #textnodes = text_to_textnodes(text)
    #htmlnodes = []
    #for textnode in textnodes:
        #html = textnode.text_node_to_html_node()
        #htmlnodes.append(html)
    #print(f"Heading Nodes: {heading_to_htmlnode(heading)}")
    #print(f"Textnodes: {textnodes}")
    #print(f"HTMLnodes: {htmlnodes}")
    #print(f"Function Test: {text_to_children(text)}")
    #print(f"Blocktype: {block_to_block_type(heading)}")
    #print(f"Markdown: {markdown_to_html_node(heading)}")
    paragraph = "This is a paragraph with **bold text** and *italic text*"
    ParaNode = paragraph_to_htmlnode(paragraph)
    #print(f"Paragraph Test: {paragraph_to_htmlnode(paragraph)}")
    #print(f"Paragraph function Test: {markdown_to_html_node(paragraph)}")
    #quote = "> This is a quote\n> This still is\n> But now with **bold text** and *italic text*"
    #print(f"Quote Test: {markdown_to_html_node(quote)}")
    #code = "```\nThis is code and this is code\nAnd this is **bold code** that should stay the same\n```"
    #print(f"Code Test: {code_to_htmlnode(code)}")
    OL = "1. This and **Bold Item 1**\n2. Item 2\n3. Item 3"
    OLNode = ordered_list_to_htmlnode(OL)
    print(f"OL Test: {ordered_list_to_htmlnode(OL)}")
    print(f"To Html: {OLNode.to_html()}")
main()

