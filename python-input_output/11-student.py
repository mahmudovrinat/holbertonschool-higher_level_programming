#!/usr/bin/python3
"""
Defines a Student class with methods for JSON serialization
and deserialization.
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
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance with those
        from the json dictionary.

        Args:
            json (dict): Dictionary containing attributes to update.
        """
        for key, value in json.items():
            setattr(self, key, value)
