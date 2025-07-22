#This class represents nodes in DOM at block or inline level 

class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children #list of HTMLNode objects
        self.props = props #dictonary representing tag attributes
    
    #children should overwrite this
    def to_html(self):
        raise NotImplementedError("to_html not implemented")
    
    def props_to_html(self):
        html = ""
        if self.props:
            for key, value in self.props.items():
                html += f' {key}="{value}"'
        return html
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})'

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("invalid HTML: no value (LeafNode requires a value)")
        if self.tag == None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("invalid HTML: no tag (ParentNode requires a tag)")
        if self.children == None:
            raise ValueError("invalid HTML: no children (ParentNode requires children)")
        children_str = ""
        for child in self.children:   
            children_str += child.to_html()
        return f'<{self.tag}{self.props_to_html()}>{children_str}</{self.tag}>'
    
    def __repr__(self):
        return f'ParentNode({self.tag}, children: {self.children}, {self.props})'