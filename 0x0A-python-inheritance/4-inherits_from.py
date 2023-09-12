#!/usr/bin/python3
"""object is an instance of inherited class
"""


def inherits_from(obj, a_class):
    """checks if object is instance of
    inherited class

    args:
        obj: first parameter
        a_class: second parameter

    Return:
        True or False
    """
    if issubclass(type(obj), a_class) and not type(obj) is a_class:
        return True
    return False
