import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_print_node(self):
        print(HTMLNode())

    def test_print_random(self):
        print(HTMLNode("asdasd","asdd","asdasd","hii"))

    def test_prop(self):
        prop = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        temp_node = HTMLNode(props = prop)
        print (temp_node.props_to_html())
        print(temp_node)
if __name__ == "__main__":
    unittest.main()
