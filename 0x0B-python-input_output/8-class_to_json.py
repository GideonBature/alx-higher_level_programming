#!/usr/bin/python3
"""CLass to JSON
"""


def class_to_json(obj):
    """Returns dictionary description with simple data structure
    for JSON serialization of an object

    Args:
        obj: an  instance of a Class

    Returns:
        Simple data structure(list, dictionary, string, integer
        and boolean
    """
    if isinstance(obj, (int, float, bool, str)):
        return obj
    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
