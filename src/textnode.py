from enum import Enum

class TextType(Enum):
    NORMAL = "normal"   #"normal"
    BOLD = "bold"       #"**bold**"
    ITALIC = "italic"   #"*italic*"
    CODE = "code"       #"``` <\n> code <\n> ```"
    LINK = "link"       #"[link](url)"
    IMAGE = "image"     #"![alt text for image](url)"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(TextNode1, TextNode2):
        if (TextNode1.text == TextNode2.text and
            TextNode1.text_type == TextNode2.text_type and
            TextNode1.url == TextNode2.url):
            return True
        return False

    def __repr__(self):
        return (f"TextNode({self.text}, {self.text_type.value}, {self.url})")

