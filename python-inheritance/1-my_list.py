#!/usr/bin/python3
"""
This module defines the MyList class that inherits from list.
"""


class MyList(list):
    """
    A custom list class that can print itself sorted.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        print(sorted(self))
