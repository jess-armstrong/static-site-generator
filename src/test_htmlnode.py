import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_print(self):
        node = HTMLNode("p", "this is a paragraph")
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, this is a paragraph, children: None, None)"
        )

    def test_print_children(self):
        child_node1 = HTMLNode("this is child 1")
        child_node2 = HTMLNode("this is child 2")
        children_nodes = [child_node1, child_node2]
        node = HTMLNode("p", "this is a paragraph", children_nodes)
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, this is a paragraph, children: [HTMLNode(this is child 1, None, children: None, None), HTMLNode(this is child 2, None, children: None, None)], None)"
        )

    def test_print_props(self):
        props = {
            "property1": "test property",
        }
        node = HTMLNode("p", "this is a paragraph", None, props)
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, this is a paragraph, children: None, {'property1': 'test property'})"
        )
    
    def test_props_to_html(self):
        props = {
            "property1": "test property",
            "property2": "test2"
        }
        node = HTMLNode("p", "this is a paragraph", None, props)
        self.assertEqual(
            node.props_to_html(),
            ' property1="test property" property2="test2"'
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_props(self):
        node = LeafNode("a", "Hello, world!", {"href": "https://www.amazon.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.amazon.com">Hello, world!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()