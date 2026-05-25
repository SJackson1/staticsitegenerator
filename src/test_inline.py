import unittest
from inline import split_nodes_delimiter,extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_plain(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.PLAIN),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.PLAIN),
        ])

    def test_double(self):
        node = TextNode("This is text with _more than one_ word _that is italic_", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("This is text with ", TextType.PLAIN),
            TextNode("more than one", TextType.ITALIC),
            TextNode(" word ", TextType.PLAIN),
            TextNode("that is italic", TextType.ITALIC),
        ])

    def test_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.PLAIN),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.PLAIN),
        ])

    def test_regex_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
            )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_regex_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
            )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)


    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode(
                    "second image", TextType.IMAGES, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )


    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                 TextNode("This is text with a link ", TextType.PLAIN),
                 TextNode("to boot dev", TextType.LINKS, "https://www.boot.dev"),
                 TextNode(" and ", TextType.PLAIN),
                 TextNode(
                     "to youtube", TextType.LINKS, "https://www.youtube.com/@bootdotdev"
                 ),
             ],
            new_nodes,
        )

    def test_ttn_plain(self):
        nodes = text_to_textnodes("This is just a simple plain text sentence")
        self.assertListEqual(nodes,[
            TextNode("This is just a simple plain text sentence", TextType.PLAIN),
        ])

    def test_ttn_italic(self):
        nodes = text_to_textnodes("This is a sentence with _italic_ words.")
        self.assertListEqual(nodes,[
            TextNode("This is a sentence with ", TextType.PLAIN), TextNode("italic", TextType.ITALIC), TextNode(" words.", TextType.PLAIN)
        ])

    def test_ttn_bold(self):
        nodes = text_to_textnodes("This is a sentence with **bold** words.")
        self.assertListEqual(nodes,[
            TextNode("This is a sentence with ", TextType.PLAIN), TextNode("bold", TextType.BOLD), TextNode(" words.", TextType.PLAIN)
        ])

    def test_ttn_bold(self):
        nodes = text_to_textnodes("This is a sentence with `code` words.")
        self.assertListEqual(nodes,[
            TextNode("This is a sentence with ", TextType.PLAIN), TextNode("code", TextType.CODE), TextNode(" words.", TextType.PLAIN)
        ])

    def test_ttn_link(self):
        nodes = text_to_textnodes("This is a sentence with [link](https://boot.dev)")
        self.assertListEqual(nodes,[
            TextNode("This is a sentence with ", TextType.PLAIN), TextNode("link", TextType.LINKS,"https://boot.dev")
        ])

    def test_ttn_image(self):
        nodes = text_to_textnodes("This is a sentence with ![image](https://boot.dev)")
        self.assertListEqual(nodes,[
            TextNode("This is a sentence with ", TextType.PLAIN), TextNode("image", TextType.IMAGES,"https://boot.dev")
        ])


    def test_text_to_nodes(self):
            nodes = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
            self.assertListEqual(nodes,[
                TextNode("This is ", TextType.PLAIN),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.PLAIN),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.PLAIN),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.PLAIN),
                TextNode("obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.PLAIN),
                TextNode("link", TextType.LINKS, "https://boot.dev"),
            ])
