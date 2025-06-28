#!/usr/bin/python3
"""Module that defines MyList class inheriting from list."""


class MyList(list):
    """MyList class inherits from list and adds a print_sorted method."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
