#!/usr/bin/python3
"""Defines BaseGeometry class with area and integer_validator methods."""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raise Exception since area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer > 0.

        Args:
            name (str): parameter name
            value: parameter value

        Raises:
            TypeError: if value is not int (exact type)
            ValueError: if value <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
