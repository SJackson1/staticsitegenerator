class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None or self.props == "":
            return ""
        else:
            built_string = []
            for attribute in self.props:
                built_string.append(f' {attribute}="{self.props[attribute]}"')
            return "".join(built_string)

    def __repr__(self):
        return (f"HTMLNode: tag={self.tag}, value={self.value}, children={self.children}, props={self.props}")

class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        super().__init__(tag,value,None,props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        elif self.tag == None:
            return str(self.value)
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self):
        return (f"HTMLNode: tag={self.tag}, value={self.value}, props={self.props}")

class ParentNode(HTMLNode):
    def __init__(self,tag,children,props = None):
        super().__init__(tag,None,children,props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("parent node must have tag")
        elif self.children is None:
            raise ValueError("children must exist and have a value")
        else:
            string_construct = f'<{self.tag}>'
            for child in self.children:
                string_construct += child.to_html()
            string_construct += f'</{self.tag}>'
            return string_construct
