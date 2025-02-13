"""import unittest

from htmlnode import ParentNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode("a", 17, {"key","value"})
        node2 = ParentNode("a", 17,{"key","value"})
        self.assertEqual(node, node2)

    def test_eq_props_none_default(self):
        node = ParentNode("b", 3, None)
        node2 = ParentNode("b", 3, None)
        self.assertEqual(node, node2)

    def test_noteq_props(self):
        node = ParentNode("c", 4, {"key","value"})
        node2 = ParentNode("c", 4, {"key","wert"})
        self.assertNotEqual(node, node2)

    def test_noteq_value(self):
        node = ParentNode("e",5, [])
        node2 = ParentNode("e",6, [])
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()"""