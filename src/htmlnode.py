
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    #def props_to_html(self):
        #html_string = ""
        #if not self.props:
            #return html_string
        #for key, value in self.props.items():
            #html_string += f' {key}="{value}"'
        #return html_string
    
    def props_to_html(self):
        if not self.props:
            return ""
        return "".join([f' {key}="{value}"' for key, value in self.props.items()])
    
    def __eq__(HTMLNode1, HTMLNode2):
        if (HTMLNode1.tag == HTMLNode2.tag and
            HTMLNode1.value == HTMLNode2.value and
            HTMLNode1.children == HTMLNode2.children and
            HTMLNode1.props == HTMLNode2.props):
            return True
        return False
        
    def  __repr__(self):
        return (f"Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props}")
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode requires a value.")
        super().__init__(tag, value, [], props)

    #@property
    #def children(self):
        #return [] # Always return an empty list for 'children'
        
    #@children.setter
    #def children(self, value):
        #raise AttributeError("Cannot add children to a LeafNode.")

    def __eq__(LeafNode1, LeafNode2):
        if (LeafNode1.tag == LeafNode2.tag and
            LeafNode1.value == LeafNode2.value and
            LeafNode1.props == LeafNode2.props):
            return True
        return False

    def to_html(self):
        if self.value is None:
            raise ValueError("Leafnode requires a value.")
        elif self.tag is None:
            return f"{self.value}"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, [], children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Object has no tag.")
        elif not self.children:
            raise ValueError("Children Value is Missing.")
        else:
            html_string = ""
            for child in self.children:
                if child.tag:
                    html_string += f"<{child.tag}>{child.value}</{child.tag}>"
                elif child.tag is None:
                    html_string += f"{child.value}"
            child.to_html()
        return f"<{self.tag}>{html_string}</{self.tag}>"
    