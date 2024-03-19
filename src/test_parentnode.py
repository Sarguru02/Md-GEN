import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_parent_node(self):
        parent = ParentNode(tag="p", children=[
            LeafNode(tag="b", value="Bold text"),
            LeafNode(value="Normal text"),
            LeafNode(tag="i", value="italic text"),
            LeafNode(value="Normal text")
                    ])
        self.assertEqual(parent.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_nesting(self):
        parent = ParentNode(tag="div", children=[
            ParentNode(tag="div", children=[
                LeafNode(tag="p", value="child of div of div"),
                LeafNode(tag="span", value="child2 of div of div")
                ]),
            LeafNode(tag="p", value="Hello"),
            ])
        self.assertEqual(parent.to_html(), "<div><div><p>child of div of div</p><span>child2 of div of div</span></div><p>Hello</p></div>")

    def test_props(self):
        parent = ParentNode(tag="div", children=[
            LeafNode(tag="h1", value="Heading 1"),
            LeafNode(tag="span", value="Span content", props={"class": "highlight-text"})
            ], props={"class": "container"})
        self.assertEqual(parent.to_html(), '<div class="container"><h1>Heading 1</h1><span class="highlight-text">Span content</span></div>')
