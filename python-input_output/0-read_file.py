#!/usr/bin/python3
"""
Module 0-read_file
Reads a UTF-8 text file and prints its content to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints it to stdout.

    Args:
        filename (str): The path to the file to read.

    No exception handling for file not found or permission errors is required.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
