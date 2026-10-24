import json
import os

def load_json_file(file_path):
    """
    Load a JSON file and return its content as a Python object.

    :param file_path: Path to the JSON file.
    :return: Python object representing the JSON data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON from the file {file_path}: {e}")

    return data