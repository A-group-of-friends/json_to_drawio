# diagram_director.py

from diagram_builder import DiagramBuilder

class DiagramDirector:
    """
    A class used to direct the creation of a diagram from JSON data.

    Attributes
    ----------
    json_data : dict
        The JSON data used to create the diagram.

    Methods
    -------
    create_diagram()
        Creates a diagram using the DiagramBuilder class and returns the built diagram.
    """

    def __init__(self, json_data):
        self.json_data = json_data

    def create_diagram(self):
        """
        Creates a diagram using the JSON data provided to the DiagramDirector object.

        Returns:
        The built diagram as a DrawIO XML string.
        """
        # Use DiagramBuilder to create the diagram
        diagram_builder = DiagramBuilder(self.json_data)
        parsed_data = diagram_builder.parse_data()
        diagram_builder.build_diagram(parsed_data)

        # Retrieve and return the built diagram
        return diagram_builder.get_diagram()