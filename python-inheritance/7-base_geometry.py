#!/usr/bin/python3
"""
Module defines BaseGeometry class with area and integer_validator methods.
"""


class BaseGeometry:
    """BaseGeometry class with area and integer validation."""

    def area(self):
        """Raises an Exception because area is not implemented yet."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is an integer greater than 0.

        Args:
            name (str): The name of the parameter.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
