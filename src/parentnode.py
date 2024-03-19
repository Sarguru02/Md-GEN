from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, children, tag=None,  props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is not provided")
        if self.children is None:
            raise ValueError("Children is not provided")
        a = ''
        for i in self.children:
            a += str(i.to_html())
        return f'<{self.tag}{super().props_to_html()}>{a}</{self.tag}>'
