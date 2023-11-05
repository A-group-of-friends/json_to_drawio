# diagram_builder.py

from json_parser import JSONParser
from drawio_builder import DrawIODiagramBuilder

class DiagramBuilder:
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
