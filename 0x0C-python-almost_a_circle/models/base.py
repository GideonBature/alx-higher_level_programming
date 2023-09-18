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
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = "[]"

        dict_objs = [obj.to_dictionary() for obj in list_objs]

        file_name = f"{cls.__name__}.json"
        json_string = cls.to_json_string(dict_objs)

        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or not json_string:
            return '[]'
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        rectangle = cls(9, 4, 1, 4)
        rectangle.update(**dictionary)
        return rectangle
