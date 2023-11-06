# drawio_element.py

import xml.etree.ElementTree as ET

import xml.etree.ElementTree as ET

class DrawIOElement:
    """
    A class representing a DrawIO element.

    Attributes:
        elem (xml.etree.ElementTree.Element): The XML element representing the DrawIO element.
    """

    def __init__(self):
        self.elem = ET.Element('mxCell')

    def add_child(self, child):
            """
            Adds a child element to the current element.

            Args:
                child (DrawIOElement): The child element to add.
            """
            self.elem.append(child.elem)
