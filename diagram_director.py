# diagram_director.py

from diagram_builder import DiagramBuilder

class DiagramDirector:
    def __init__(self, json_data):
        self.json_data = json_data

    def create_diagram(self):
        # Use DiagramBuilder to create the diagram
        diagram_builder = DiagramBuilder(self.json_data)
        parsed_data = diagram_builder.parse_data()
        diagram_builder.build_diagram(parsed_data)

        # Retrieve and return the built diagram
        return diagram_builder.get_diagram()