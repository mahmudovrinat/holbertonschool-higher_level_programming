#!/usr/bin/python3
"""
Module 1-write_file
Writes a string to a UTF-8 text file and returns the number of characters
written.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF-8) and return the number of characters
    written.

    Args:
        filename (str): The file path to write to.
        text (str): The string to write.

    Returns:
        int: Number of characters written to the file.

    The function creates the file if it doesn't exist and overwrites it if it
    does. No exception handling for file permissions is required.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
