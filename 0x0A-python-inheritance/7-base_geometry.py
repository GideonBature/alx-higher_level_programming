#!/usr/bin/python3
"""a class with instance method
"""


class BaseGeometry:
    """a base class
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate name as str and value as int

        Args:
            name (str): name of parameter
            value (int): parameter to validate
        Raises:
            TypeError: If value is not an integer
            ValueError: if value is <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
