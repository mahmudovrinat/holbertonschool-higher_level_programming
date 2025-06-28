#!/usr/bin/python3
"""
Module 2-append_write
Appends a string at the end of a UTF-8 text file and returns the number of
characters added.
"""


def append_write(filename="", text=""):
    """
    Append a string to a text file (UTF-8) and return the number of characters
    added.

    Args:
        filename (str): The file path to append to.
        text (str): The string to append.

    Returns:
        int: Number of characters added to the file.

    The function creates the file if it doesn't exist.
    No exception handling for file permissions or missing file is required.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
