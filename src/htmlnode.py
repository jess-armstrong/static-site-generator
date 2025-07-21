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