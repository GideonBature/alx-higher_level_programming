#!/usr/bin/python3
"""list of available attributes and methods
"""
def lookup(obj):
    """list of attributes and methods of objs

    Args:
        obj - parameter

    Return:
        list
    """
    return dir(obj)
