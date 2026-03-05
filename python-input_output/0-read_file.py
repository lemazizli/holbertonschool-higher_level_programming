#!/usr/bin/python3
"""
read_file funksiyasini isleden modul
"""


def read_file(filename=""):
    """
    this is a read_file function.

    parametrs: filename
    """
    if not filename:
        return
    with open(filename, "r") as file:
        print(file.read(), end="")
