#!/usr/bin/python3
"""object an instance of class
"""


def is_same_class(obj, a_class):
    """checks if object is instance of class

    args:
        obj: first parameter
        a_class: second parameter

    Return:
        True or False
    """
    if type(obj) is a_class:
        return True
    return False
