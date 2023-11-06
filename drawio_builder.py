# drawio_builder.py

import xml.etree.ElementTree as ET
from drawio_element import DrawIOElement
from package_element import PackageElement
from class_element import ClassElement

class DrawIODiagramBuilder:
    """
    A class used to build a DrawIO diagram from parsed JSON data.

    Attributes
    ----------
    root : xml.etree.ElementTree.Element
        The root element of the mxfile.
    mxCell : xml.etree.ElementTree.Element
        The mxCell element of the mxGraphModel.

    Methods
    -------
    build(parsed_data)
        Builds the DrawIO diagram from parsed JSON data.
    _add_elements(parent, data)
        Recursively adds elements to the diagram.
    """
    def __init__(self):
        self.root = ET.Element('mxfile', host="app.diagrams.net")
        diagram = ET.SubElement(self.root, 'diagram', id="DyfSqh4o6D0qI5xqRX0x", name="Page-1")
        mxGraphModel = ET.SubElement(diagram, 'mxGraphModel', dx="1050", dy="465", grid="1", gridSize="10",
                                     guides="1", tooltips="1", connect="1", arrows="1", fold="1", page="1",
                                     pageScale="1", pageWidth="827", pageHeight="1169", math="0", shadow="0")
        root = ET.SubElement(mxGraphModel, 'root')
        parent = ET.SubElement(root, 'mxCell', id="0")
        self.mxCell = ET.SubElement(root, 'mxCell', id="1", parent="0")
