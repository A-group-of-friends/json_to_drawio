# diagram_builder.py

from json_parser import JSONParser
from drawio_builder import DrawIODiagramBuilder

class DiagramBuilder:
    """
    A class used to build a DrawIO diagram from JSON data.

    Attributes
    ----------
    json_data : str
        The JSON data to be parsed and used to build the diagram.
    diagram : DrawIO.Diagram
        The resulting DrawIO diagram.

    Methods
    -------
    parse_data()
        Parses the JSON data and returns the parsed data.
    build_diagram(parsed_data)
        Builds the DrawIO diagram from the parsed data.
    get_diagram()
        Returns the resulting DrawIO diagram.
    """

    def __init__(self, json_data):
        self.json_data = json_data
        self.diagram = None
    
    def parse_data(self):
        parser = JSONParser(self.json_data)
        return parser.parse()
    
    def build_diagram(self, parsed_data):
        builder = DrawIODiagramBuilder()
        self.diagram = builder.build(parsed_data)
    
    def get_diagram(self):
        return self.diagram
