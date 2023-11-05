# package_element.py

from drawio_element import DrawIOElement

class PackageElement(DrawIOElement):
    def __init__(self, name):
        super().__init__()
        self.elem.attrib = {'style': 'shape=package;', 'value': name}