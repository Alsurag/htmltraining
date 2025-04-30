class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None:
            return ""
        return "".join([f' {key}="{value}"' for key, value in self.props.items()])
    
    def __repr__(self):
        parts = ["HTMLNode"]

        if self.tag:
            parts.append(f"tag='{self.tag}'")

        if self.value:
            preview = self.value if len(self.value) < 20 else self.value[:17] + "..."
            parts.append(f"value='{preview}'")
        
        if self.children:
            parts.append(f"children={len(self.children)} items")

        if self.props:
            parts.append(f"props={self.props}")
        
        return ", ".join(parts) + ")"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):        
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        
        if self.tag is None:
            return self.value
        
        html = f"<{self.tag}"
        
        if self.props:
            for prop, value in self.props.items():
                html += f' {prop}="{value}"'    
        
        html += f">{self.value}</{self.tag}>"
        
        return html

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError ("ParentNode must have a tag")
        
        if self.children is None:
            raise ValueError ("ParentNode must have children")
        
        props_str = ""
        if self.props:
            props_str = " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())
        
        opening_tag = f"<{self.tag}{props_str}>"
        
        children_html = "".join(child.to_html() for child in self.children)
        return f"{opening_tag}{children_html}</{self.tag}>"