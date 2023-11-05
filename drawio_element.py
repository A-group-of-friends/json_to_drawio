# drawio_element.py

import xml.etree.ElementTree as ET

class DrawIOElement:
    def __init__(self):
        self.elem = ET.Element('mxCell')

    def add_child(self, child):
        self.elem.append(child.elem)
