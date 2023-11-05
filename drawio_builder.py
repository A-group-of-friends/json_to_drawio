# drawio_builder.py

import xml.etree.ElementTree as ET
from drawio_element import DrawIOElement
from package_element import PackageElement
from class_element import ClassElement

class DrawIODiagramBuilder:
    def __init__(self):
        self.root = ET.Element('mxfile', host="app.diagrams.net")
        diagram = ET.SubElement(self.root, 'diagram', id="DyfSqh4o6D0qI5xqRX0x", name="Page-1")
        mxGraphModel = ET.SubElement(diagram, 'mxGraphModel', dx="1050", dy="465", grid="1", gridSize="10",
                                     guides="1", tooltips="1", connect="1", arrows="1", fold="1", page="1",
                                     pageScale="1", pageWidth="827", pageHeight="1169", math="0", shadow="0")
        root = ET.SubElement(mxGraphModel, 'root')
        parent = ET.SubElement(root, 'mxCell', id="0")
        self.mxCell = ET.SubElement(root, 'mxCell', id="1", parent="0")
    
    def build(self, parsed_data):
        self._add_elements(self.mxCell, parsed_data)
        return ET.tostring(self.root).decode()
    
    def _add_elements(self, parent, data):
        for key, value in data.items():
            if isinstance(value, dict):
                package_elem = PackageElement(key)
                parent.append(package_elem.elem)
                self._add_elements(package_elem.elem, value)
            else:
                class_elem = ClassElement(key)
                parent.append(class_elem.elem)
