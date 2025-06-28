#!/usr/bin/python3
"""
Defines a Student class with public attributes and a method
to return dictionary representation of the instance with
optional filtering by attribute names.
"""


class Student:
    """
    Represents a student with first name, last name and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name (str): Student's first name.
            last_name (str): Student's last name.
            age (int): Student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): List of attribute names to retrieve.
                If None or not a list, return all attributes.

        Returns:
            dict: Dictionary containing requested attributes.
        """
        if isinstance(attrs, list):
            # Filter only attributes in attrs and that exist on instance
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        else:
            # Return all attributes
            return self.__dict__.copy()
