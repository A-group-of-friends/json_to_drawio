# class_element.py

from drawio_element import DrawIOElement

class ClassElement(DrawIOElement):
    def __init__(self, name):
        super().__init__()
        self.elem.attrib = {'style': 'shape=class;', 'value': name}
