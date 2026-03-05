#!/usr/bin/python3
"""
defines a student class with json serialization and optional filtering.
"""


class Student:
    """Represents a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with her first_name, last_name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        return a dict represention of student.

        kc;kesdfgdsalokn mlo,kcfkn dlc lsjdke cf
        eknwf cwlnekfn w;ekfnew;k
        """
        if attrs is None:
            return self.__dict__.copy()
        return {key: self.__dict__[key] for key in attrs if key in self.__dict__}
