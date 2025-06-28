#!/usr/bin/python3
"""Module defining BaseGeometry with unimplemented area method."""


class BaseGeometry:
    """BaseGeometry class with area method not implemented."""

    def area(self):
        """Raise an exception indicating area is not implemented."""
        raise Exception("area() is not implemented")
