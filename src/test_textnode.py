import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)


    def test_noteq(self):
        node3 = TextNode("This is a different", TextType.BOLD)
        node = TextNode("From this", TextType.BOLD)
        self.assertNotEqual(node, node3)

    def test_eq2(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        node2 = TextNode("This is a text node", TextType.PLAIN)
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is a text node", TextType.PLAIN, None)
        node2 = TextNode("This is a text node", TextType.PLAIN, None)
        self.assertEqual(node, node2)
if __name__ == "__main__":
    unittest.main()
