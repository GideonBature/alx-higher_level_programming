#!/usr/bin/python3
"""Writes Object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a JSON representation

    Args:
        my_obj: the object parameter
        filename: (str): name of file

    """
    with open(filename, 'w', encoding='UTF8') as json_file:
        json.dump(my_obj, json_file)
