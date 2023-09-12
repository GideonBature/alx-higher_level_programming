#!/usr/bin/python3
"""Returns JSON representation
"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object(string)

    Args:
        my_obj: the object parameter

    """
    return json.dumps(my_obj)
