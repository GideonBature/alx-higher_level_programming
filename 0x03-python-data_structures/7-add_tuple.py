#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples

    Parameters

    tuple_a: tuple
        The first tuple
    tuple_b: tuple
        The second tuple

    Return:
        A tuple with 2 integers
    """
    result = tuple()
    if len(tuple_a) < 2:
        if len(tuple_a) == 1:
            tuple_a = tuple_a[0], 0
        else:
            tuple_a = 0, 0
    if len(tuple_b) < 2:
        if len(tuple_b) == 1:
            tuple_b = tuple_b[0], 0
        else:
            tuple_b = 0, 0

    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return result
