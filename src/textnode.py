#This class represents the types of inline text that can exist in HTML and Markdown

from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url #link or image. None by default

    #compare TextNode objects for testing
    def __eq__(self, value): 
        if self.text == value.text and self.text_type == value.text_type and self.url == value.url:
            return True
        return False
    
    #string rep of TextNode obj
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"