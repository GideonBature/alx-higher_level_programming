#!/usr/bin/python3
"""Matrix Divider
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix

    Args:
        matrix: (int/float) first parameter
        div: (int) second parameter

    Returns:
            list of lists (int/float)
    """
    for sub_list in matrix:
        if not all(isinstance(elem, (int, float)) for elem in sub_list):
            msg = "matrix must be a matrix (list of lists) of integers/floats"
            raise TypeError(msg)

    first_list_len = len(matrix[0])

    for sub_list in matrix:
        if len(sub_list) != first_list_len:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    matrix_d = [[round(float(x / div), 2) for x in row] for row in matrix]

    return matrix_d
