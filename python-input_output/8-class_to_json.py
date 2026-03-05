#!/usr/bin/python3
"""
functions returns a dictionary description of an object
for json serialization.
"""


def class_to_json(obj):
    """
    Arguments:
        obj:an instance of class
    Returns:
        dictionary of serializable attributes (instance + class)
    """
    result = {}
    for key in dir(obj):
        if key.startswith('__'):
            continue
        value = getattr(obj, key)
        if isinstance(value, (int, str, bool, float, list, dict)):
            result[key] = value
        return result
