#!/usr/bin/python3
"""Returns object(Python data structure) representation
"""
import json


def from_json_string(my_str):
    """Returns the object representation of a JSON string

    Args:
        my_str: the string parameter

    """
    return json.loads(my_str)
