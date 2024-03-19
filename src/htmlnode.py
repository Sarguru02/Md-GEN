class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        a=''
        if self.props is not None:
            for i in self.props:
                a+=f' {i}="{self.props[i]}"'
            return a
        return ''

    def __repr__(self) -> str:
        return f"tag:{self.tag}\nvalue:{self.value}\nchildren:{self.children}\nprops:{self.props}"
