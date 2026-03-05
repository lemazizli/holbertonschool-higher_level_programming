#!/usr/bin/python3
"""
in this module containing write_file function
"""


def write_file(filename="", text=""):
    """
    this is the write_file function.

    Parametrs: filename and text
    Returns: number of chars written
    """
    with open(filename, "w") as file:
        num_chars_written = file.write(text)
    return num_chars_written
