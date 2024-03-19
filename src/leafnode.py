from htmlnode import HTMLNode
class LeafNode(HTMLNode):
    def __init__(self,value,tag=None,  children=None, props=None ):
        super().__init__(tag, value, children, props)

    def to_html(self):
        if self.tag is None:
            return self.value
        if self.value:
            prop_string = super().props_to_html()
            out = f'<{self.tag}{prop_string}>{self.value}</{self.tag}>'
            return out
        else:
            raise ValueError("All leaf nodes require a value")
