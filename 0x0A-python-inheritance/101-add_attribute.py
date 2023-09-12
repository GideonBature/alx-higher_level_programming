#!/usr/bin/python3
"""Function that adds attribute to object
"""


def add_attribute(obj, name, value):
    """Add attributes to object

    Args:
        obj: object
        name (str): name of attribute
        value (int/str): value of the attribute
    """
    if "__slots__" in dir(obj) or hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
