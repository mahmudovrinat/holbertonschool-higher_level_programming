#!/usr/bin/python3
"""
Module 4-from_json_string
Returns the Python object represented by a JSON string.
"""

import json


def from_json_string(my_str):
    """
    Return the Python object represented by a JSON string.

    Args:
        my_str (str): A JSON string.

    Returns:
        The Python object represented by the JSON string.

    No exception handling required for invalid JSON strings.
    """
    return json.loads(my_str)
