#!/usr/bin/python3
"""create an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file

    Args:
        filename: (str): the string parameter

    """
    with open(filename, 'r', encoding='UTF8') as json_file:
        return json.load(json_file)
