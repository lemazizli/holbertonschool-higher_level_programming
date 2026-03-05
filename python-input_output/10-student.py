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
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            res = {}
            for a in attrs:
                if a in self.__dict__:
                    res[a] = self.__dict__[a]
            return res
        return self.__dict__
