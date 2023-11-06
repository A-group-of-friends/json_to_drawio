# class_element.py

from drawio_element import DrawIOElement

class ClassElement(DrawIOElement):
    """
    Represents a class element in a DrawIO diagram.

    Attributes:
    - name (str): The name of the class.
    """
    def __init__(self, name):
        super().__init__()
        self.elem.attrib = {'style': 'shape=class;', 'value': name}
