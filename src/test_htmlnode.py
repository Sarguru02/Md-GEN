import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_properties(self):
        node = HTMLNode(tag='div', props={'id': 'mydiv'})
        self.assertEqual(node.tag, 'div')
        self.assertEqual(node.props, {'id': 'mydiv'})

    def test_props_to_html(self):
        node1 = HTMLNode(tag='div', props={'id': 'mydiv'})
        self.assertEqual(node1.props_to_html(), ' id="mydiv"')
