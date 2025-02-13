import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", 17, None, {"key","value"})
        node2 = HTMLNode("a", 17, None, {"key","value"})
        self.assertEqual(node, node2)

    def test_eq_props_none_default(self):
        node = HTMLNode("b", 3, "Child", None)
        node2 = HTMLNode("b", 3, "Child")
        self.assertEqual(node, node2)

    def test_noteq_props(self):
        node = HTMLNode("c", 4, "Child", {"key","value"})
        node2 = HTMLNode("c", 4, "Child", {"key","wert"})
        self.assertNotEqual(node, node2)

    def test_noteq_value(self):
        node = HTMLNode("e",5,"Child")
        node2 = HTMLNode("e",6,"Child")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()