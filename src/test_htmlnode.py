import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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
    ## LEAFNODE TESTS ##
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_props(self):
        node = LeafNode("a", "Hello, world!", {"href": "https://www.amazon.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.amazon.com">Hello, world!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    ## PARENTNODE TESTS ##
    def test_parent_to_html(self):
        children = [LeafNode("p", "Hello, world!")]
        node = ParentNode("h1", children)
        self.assertEqual(node.to_html(), '<h1><p>Hello, world!</p></h1>')

    def test_parent_to_html_more_children(self):
        children = [LeafNode("p", "Hello, world!"), LeafNode("b", "bold!")]
        node = ParentNode("h1", children)
        self.assertEqual(node.to_html(), '<h1><p>Hello, world!</p><b>bold!</b></h1>')

    def test_parent_to_html_no_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode("h1", None)
            node.to_html()        

    def test_parent_to_html_props(self):
        children = [LeafNode("p", "Hello, world!")]
        node = ParentNode("a", children, {"href": "https://www.amazon.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.amazon.com"><p>Hello, world!</p></a>')

    def test_parent_to_html_grandchildren(self):
        grandchildren = [LeafNode("b", "Hello, world!")]
        children = [ParentNode("p", grandchildren)]
        node = ParentNode("h1", children)
        print(node.to_html())
        self.assertEqual(node.to_html(), '<h1><p><b>Hello, world!</b></p></h1>')

if __name__ == "__main__":
    unittest.main()