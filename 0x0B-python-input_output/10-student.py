#!/usr/bin/python3
"""Student to JSON with filter
"""


class Student:
    """Student class
    """
    def __init__(self, first_name, last_name, age):
        """Instantiates public attributes

        Args:
            first_name (str): first name parameter
            last_name (str): last name parameter
            age: (int) age parameter
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of
        a Student instance.

        Returns:
        dict: A dictionary with the student's information
        """
        if attrs is None:
            return {"first_name": self.first_name,
                    "last_name": self.last_name,
                    "age": self.age
                    }
        else:
            s = {attr: getattr(self, attr) for attr
                 in attrs if hasattr(self, attr)}
            return s
