import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_node(self):
        leaf = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(leaf.to_html(), '<a href="https://www.google.com">Click me!</a>')
        leaf1 = LeafNode(tag="p", value="This is a paragraph of text.")
        self.assertEqual(leaf1.to_html(), '<p>This is a paragraph of text.</p>')

    def test_without_tag(self):
        leaf = LeafNode(value="Hello")
        self.assertEqual(leaf.to_html(), "Hello")
