#!/usr/bin/python3
import numpy as np
"""
testing another coment.
"""
def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        list of lists: The result of matrix multiplication.

    Raises:
        ValueError: If matrices are not valid for multiplication.

    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise ValueError("m_a must be a list and m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise ValueError("m_a must be a list of lists and m_b must be a list of lists")

    if not m_a or not m_b:
        raise ValueError("m_a can't be empty and m_b can't be empty")

    if any(not isinstance(num, (int, float)) for row in m_a for num in row) or any(not isinstance(num, (int, float)) for row in m_b for num in row):
        raise ValueError("m_a should contain only integers or floats and m_b should contain only integers or floats")

    if any(len(row) != len(m_a[0]) for row in m_a) or any(len(row) != len(m_b[0]) for row in m_b):
        raise ValueError("Each row of m_a must be of the same size and each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    matrix_a = np.array(m_a)
    matrix_b = np.array(m_b)
    result = np.matmul(matrix_a, matrix_b)

    return result.tolist()
