#!/usr/bin/python3
"""
This module defines a function to load an object from
a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        The Python object deserialized from the JSON file.

    Raises:
        FileNotFoundError: If the file does not exist.
        JSONDecodeError: If the file contains invalid JSON.
    """
    with open(filename, 'r') as f:
        return json.load(f)
