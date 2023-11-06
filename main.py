
from diagram_director import DiagramDirector

def main():
    """
    This function takes a JSON data as input, creates a diagram using DiagramDirector, and prints the built diagram.
    """
    # Sample JSON data
    json_data = {
        "app": {
            "api": {
                "test_api.py": "all the code in the test_api.py file",
                "auth": {
                    "login.py": "code for login"
                }
            },
            "config.py": "all the code for the config file"
        }
    }

    # Use DiagramDirector to create and retrieve the diagram
    diagram_director = DiagramDirector(json_data)
    xml_str = diagram_director.create_diagram()

    # Print the built diagram
    print(xml_str)

# This ensures that main() is only called when this script is executed directly
if __name__ == "__main__":
    main()