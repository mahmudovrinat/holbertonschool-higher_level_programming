#!/usr/bin/python3
"""
Module 0-lookup
Defines a function that returns available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        List of strings representing attributes and methods of obj.
    """
    return dir(obj)
