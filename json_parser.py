# json_parser.py

import json

class JSONParser:
    """
    A class used to parse JSON data.
    
    Attributes
    ----------
    json_data : str
        The JSON data to be parsed.
    """
    def __init__(self, json_data):
        self.json_data = json_data
    
    def parse(self):
        """
        Parses the JSON data and returns it as a Python object.
        
        Returns
        -------
        object
            The parsed JSON data as a Python object.
        """
        return self.json_data
