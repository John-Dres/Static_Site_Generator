import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("a", 17, {"key","value"})
        node2 = LeafNode("a", 17,{"key","value"})
        self.assertEqual(node, node2)

    def test_eq_props_none_default(self):
        node = LeafNode("b", 3, None)
        node2 = LeafNode("b", 3, None)
        self.assertEqual(node, node2)

    def test_noteq_props(self):
        node = LeafNode("c", 4, {"key","value"})
        node2 = LeafNode("c", 4, {"key","wert"})
        self.assertNotEqual(node, node2)

    def test_noteq_value(self):
        node = LeafNode("e",5, [])
        node2 = LeafNode("e",6, [])
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()