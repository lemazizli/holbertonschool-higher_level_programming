#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The 0-add_integer module supplies one function, add_integer(a, b).
For example, it can be used to add two integers like 1 and 2.
This module is designed for the Test Driven Development project.
It handles integers and floats, and performs necessary type checks.
"""


def add_integer(a, b=98):
    """Return the addition of a and b as integers.

    a and b must be integers or floats. Floats are cast to integers before
    performing the addition.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
