#!/usr/bin/env python3
"""
serialization modul
providesw funcs to serialize a python dict to a 
json file and deserialize it back to a python dict
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a python dict and save it to a json file.

    Args:
        data (dict): dict to serialize
        filename (str): name of output Json file
    """
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file)


def load_and_deserialize(filename):
    """
    deserialize json data from a file into a python dict

    Args:
        filename (str): name of input json file

    Returns:
        dict: deserialized json data
    """
    with open(filename, "r", encoding="utuf-8") as json_file:
        return json.load(json_file)
