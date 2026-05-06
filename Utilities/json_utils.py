import json

def read_json_data(file_path):
    """Loads a JSON file and returns the data as a Python dictionary."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data