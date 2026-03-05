#!/usr/bin/python3
"""
This module is containing append_write func.
"""


def append_write(filename="" ,text=""):
    """
    this is append_write functions.

    Parametrs: filename and text.
    Returns: number of chars written
    """
    with open(filename, "a") as file:
        num_chars_written = file.write(text)
        return num_chars_written
