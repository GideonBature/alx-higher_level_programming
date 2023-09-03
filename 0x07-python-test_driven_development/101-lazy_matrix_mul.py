#!/usr/bin/python3
"""Lazy matrix multiplication
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy.

    Args:
        m_a (numpy.ndarray): The first matrix.
        m_b (numpy.ndarray): The second matrix.

    Returns:
    numpy.ndarray: The result of multiplying m_a m_b.
    """

    matrix_a = np.array(m_a)
    matrix_b = np.array(m_b)

    if matrix_a.shape[1] != matrix_b.shape[0]:
        raise ValueError("Matrix dimensions are not compatible for multiplication.")

    result = np.dot(m_a, m_b)
    return result
