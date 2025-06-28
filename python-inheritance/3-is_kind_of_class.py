#!/usr/bin/python3
"""Module that defines a function to check if an object is an instance
or an instance of a subclass of a specified class."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or its subclass."""
    return isinstance(obj, a_class)
