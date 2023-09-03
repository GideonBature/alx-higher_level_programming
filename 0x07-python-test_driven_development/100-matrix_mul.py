#!/usr/bin/python3
"""Matrix multiplication
"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices

    Args:
        m_a (int/float): The first matrix
        m_b (int/float): The second matrix

    Returns:
        list of lists: The result of m_a * m_b
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(lists, list) for lists in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(lists, list) for lists in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise TypeError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise TypeError("m_b can't be empty")
    if check_elems(m_a):
        raise TypeError("m_a should contain only integers or floats")
    if check_elems(m_b):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("Each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("Each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m_c = [[0 for _ in range(len(m_b))] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                m_c[i][j] += m_a[i][k] * m_b[k][j]

    return m_c


def check_elems(m):
    for r in m:
        for elem in r:
            if not isinstance(elem, (int, float)):
                return True
    return False
