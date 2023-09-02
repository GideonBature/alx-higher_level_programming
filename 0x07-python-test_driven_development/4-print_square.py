#!/usr/bin/python3
""" The print square function"""


def print_square(size):
    """Prints square with #

    Args:
        size (int): the first parameter.

    Returns:
        prints a square using #
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")

        print()
