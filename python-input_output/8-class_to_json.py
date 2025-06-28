#!/usr/bin/python3
"""
This module defines a function that returns the dictionary
description with simple data structures (list, dict, str,
int, bool) for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description for JSON serialization
    of an object.

    Args:
        obj (object): Instance of a class.

    Returns:
        dict: Dictionary containing all attributes of obj.
    """
    return obj.__dict__.copy()
