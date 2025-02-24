import unittest

from myfunctions import *
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_eq_bold(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        outcome = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_outcome = [
                            TextNode('This is ', TextType.TEXT),
                            TextNode('bold', TextType.BOLD),
                            TextNode(' text', TextType.TEXT)
                            ]
        self.assertEqual(outcome, expected_outcome)
    
    def test_eq_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        outcome = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_outcome = [
                            TextNode('This is text with a ', TextType.TEXT),
                            TextNode('code block', TextType.CODE),
                            TextNode(' word', TextType.TEXT)
                            ]
        self.assertEqual(outcome, expected_outcome)

    def test_empty_list_error(self):
        with self.assertRaises(ValueError, msg="Empty list"):
            split_nodes_delimiter([], "*", TextType.TEXT)

    def test_invalid_markdown_syntax_error(self):
        node = TextNode("Invalid **bold syntax", TextType.TEXT)
        with self.assertRaises(SyntaxError, msg=f"Invalid Markdown syntax in node: '{node.text}'"):
            split_nodes_delimiter([node], "**", TextType.BOLD)






if __name__ == "__main__":
    unittest.main()