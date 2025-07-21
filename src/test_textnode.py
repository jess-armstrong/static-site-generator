import unittest
from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()