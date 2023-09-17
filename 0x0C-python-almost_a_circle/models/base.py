#!/usr/bin/python3
"""Base Class
"""
import json


class Base:
    """ The Base of all other classes in this
    project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or {}:
            return "[]"
        return json.dumps(list_dictionaries)
