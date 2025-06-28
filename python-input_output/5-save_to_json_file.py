#!/usr/bin/python3
"""
This module defines a function to save an object to a file
in JSON format.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using JSON representation.

    Args:
        my_obj (any): The object to serialize to JSON.
        filename (str): The file name where the JSON data
                        will be written.

    Raises:
        TypeError: If the object is not JSON serializable.
        OSError: If file cannot be written due to permission or
                 other OS errors.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
