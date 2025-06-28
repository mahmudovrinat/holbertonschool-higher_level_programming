#!/usr/bin/python3
"""
Defines a Student class with public attributes and a method
to return dictionary representation of the instance.
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

    def to_json(self):
        """
        Retrieve a dictionary representation of the Student instance.

        Returns:
            dict: Dictionary containing instance attributes.
        """
        return self.__dict__.copy()
