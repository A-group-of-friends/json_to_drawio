# package_element.py

from drawio_element import DrawIOElement

class PackageElement(DrawIOElement):
    """
    A class representing a package element in DrawIO.

    Attributes:
    - name (str): The name of the package.
    """
    def __init__(self, name):
        super().__init__()
        self.elem.attrib = {'style': 'shape=package;', 'value': name}