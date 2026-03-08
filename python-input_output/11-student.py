#!/usr/bin/python3
""" Student class with json serialization and deserialization"""


class Student:
    """ classdida"""

    def __init__(self, first_name, last_name, age):
        """Initialize a student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dict representation of the instance 
        If attrs is a list of strings, only return those attrs
        """
        if isinstance(attrs, list):
            new_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    new_dict[attr] = getattr(self, attr)
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attrs of the instance using a dict
        """
        for key, value in json.items():
            setattr(self, key, value)
