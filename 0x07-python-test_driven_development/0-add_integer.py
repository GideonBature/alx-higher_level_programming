#!/usr/bin/python3
"""add function
"""


def add_integer(a, b=98):
    """Add two integers

    Floats are typecasted to int

    Args:
        a (int/float): The first parameter
        b (int): The second parameter

    Returns:
        int: The return value
    """
    if not (isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if not (isinstance(b, (int, float))):
        raise TypeError("b must be an integer")

    if type(a) == float:
        a = int(a)

    if type(b) == float:
        b = int(b)

    return a + b
