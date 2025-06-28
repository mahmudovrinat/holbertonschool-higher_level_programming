#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """Base class for geometry operations."""

    def area(self):
        """Raise exception indicating area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
