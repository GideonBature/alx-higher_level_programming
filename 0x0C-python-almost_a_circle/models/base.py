#!/usr/bin/python3
"""Base Class
"""
import json
import csv


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

    @classmethod
    def load_from_file(cls):
        file_name = f"{cls.__name__}.json"

        try:
            with open(file_name, 'r', encoding='utf-8') as json_file:
                json_string = json_file.read()
                dict_list = cls.from_json_string(json_string)
                instances = [cls.create(**d) for d in dict_list]
                return instances
        except FileNotFoundError:
            return "[]"


    @classmethod
    def save_to_file_csv(cls, list_objs):
        if list_objs is None:
            list_objs = "[]"

        dict_objs = [obj.to_dictionary() for obj in list_objs]

        file_name = f"{cls.__name__}.csv"

        with open(file_name, 'w') as csv_file:
            writer = csv.writer(csv_file)

            if cls.__name__ == 'Rectangle':
                writer.writerow(['id', 'width', 'height', 'x', 'y'])

                writer.writerow(dict_objs)

            elif cls.__name__ == 'Square':
                writer.writerow(['id', 'size', 'x', 'y'])

                writer.writerow(dict_objs)

    @classmethod
    def load_from_file_csv(cls):
        file_name = f"{cls.__name__}.csv"
        instances = []

        try:
            with open(file_name, 'r') as csv_file:
                reader = csv.reader(csv_file)

                next(reader, None)

                for row in reader:
                    if cls.__name__ == 'Rectangle':
                        id, width, height, x, y = map(int, row)
                        instances.append(cls(id, width, height, x, y))
                    elif cls.__name__ == 'Square':
                        id, size, x, y = map(int, row)
                        instances.append(cls(id, size, x, y))
        except FileNotFoundError:
            return []

        return instances
