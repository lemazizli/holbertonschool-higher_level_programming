#!/usr/bin/python3
"""
this is the  module containin to_json func
"""

import json


def to_json_string(my_obj):
    """
    this is a to_json function.

    Parametrs: my_obj
    Returns: JSON representation of object (string)
    """
    json_string = json.dumps(my_obj)
    return json_string
