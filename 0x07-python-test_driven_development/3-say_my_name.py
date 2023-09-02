#!/usr/bin/python3
"""Contains the Say My Name Function"""


def say_my_name(first_name, last_name=""):
    """This function Prints:
    <first name> SPACE <last name>

    Args:
        first_name (str): The first parameter
        last_name (str): The second parameter

    Returns:
        <first name> SPACE <last name>
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("{} {}".format(first_name, last_name))
