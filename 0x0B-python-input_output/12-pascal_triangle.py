#!/usr/bin/python3
"""Pascal's Triangle
"""


def pascal_triangle(n):
    """list of lists of integers representing
    the Pascal's triangle of n

    Args:
        n (int): size of pascal triangle

    Returns:
        list of lists of integers
    """
    p_list = []
    if n <= 0:
        return p_list

    for i in range(n):
        if not p_list:
            prev_row = []
        else:
            prev_row = p_list[-1]

        row = [1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        if i > 0:
            row.append(1)

        p_list.append(row)

    return p_list
