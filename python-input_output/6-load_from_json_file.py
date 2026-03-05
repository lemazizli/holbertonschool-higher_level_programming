#!/usr/bin/python3
"""
func create an object from a json file. 
"""

import json


def load_from_json_file(filename):
    """returns a python object from json file"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
