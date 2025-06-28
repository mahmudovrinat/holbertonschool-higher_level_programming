#!/usr/bin/python3
"""
Module 3-to_json_string
Returns the JSON representation of an object (string).
"""

import json


def to_json_string(my_obj):
    """
    Return the JSON representation of a Python object.

    Args:
        my_obj: The object to serialize.

    Returns:
        str: JSON string representation of the object.

    No exception handling is required if the object is not serializable.
    """
    return json.dumps(my_obj)
