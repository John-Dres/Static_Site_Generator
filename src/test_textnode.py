import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq_url(self):
        node = TextNode("Url-Test", TextType.LINK, "www.test.de")
        node2 = TextNode("Url-Test", TextType.LINK, "www.boot.de")
        self.assertNotEqual(node, node2)

    def test_noteq_texttype(self):
        node = TextNode("TextTypeTest", TextType.TEXT, "www.test.de")
        node2 = TextNode("TextTypeTest", TextType.LINK, "www.test.de")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()