#!/usr/bin/python3
"""object is kind of class
"""


def is_kind_of_class(obj, a_class):
    """checks if object is instance of
    class or inherited class

    args:
        obj: first parameter
        a_class: second parameter

    Return:
        True or False
    """
    if type(obj) is a_class or isinstance(obj, a_class):
        return True
    return False
