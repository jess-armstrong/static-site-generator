import unittest
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("Equal text nodes", TextType.LINK)
        node2 = TextNode("Equal text nodes", TextType.LINK)
        self.assertEqual(node, node2)
        
    def test_eq_url(self):
        node = TextNode("Equal text nodes", TextType.LINK,"a link")
        node2 = TextNode("Equal text nodes", TextType.LINK, "a link")
        self.assertEqual(node, node2)
    
    def test_eq_url_none(self):
        node = TextNode("Equal text nodes", TextType.LINK, None)
        node2 = TextNode("Equal text nodes", TextType.LINK)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("Not equal text nodes", TextType.LINK)
        node2 = TextNode("This should not be equal nodes", TextType.LINK)
        self.assertNotEqual(node, node2)
    
    def test_not_eq_texttype(self):
        node = TextNode("Equal text nodes", TextType.BOLD)
        node2 = TextNode("Equal text nodes", TextType.LINK)
        self.assertNotEqual(node, node2)
    
    def test_not_eq_url(self):
        node = TextNode("Equal text nodes", TextType.LINK, "test")
        node2 = TextNode("Equal text nodes", TextType.LINK)
        self.assertNotEqual(node, node2)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "text node")

    def test_code(self):
        node = TextNode("code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "code node")
    
    def test_link(self):
        node = TextNode("link node", TextType.LINK, "https://www.youtube.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "link node")
        self.assertEqual(html_node.props, {"href": "https://www.youtube.com"})

    def test_image(self):
        node = TextNode("image node", TextType.IMAGE, "https://www.youtube.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src":"https://www.youtube.com", "alt": "image node"})

if __name__ == "__main__":
    unittest.main()