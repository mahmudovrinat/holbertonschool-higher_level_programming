#!/usr/bin/python3
"""Defines BaseGeometry class with area and integer_validator methods."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Raise exception for area not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name (str): The name of the parameter to validate.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer or is a bool.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
