#!/usr/bin/python3
"""
This module defines a function to divide all elements of a matrix by a given divisor and return a new matrix with rounded results.
"""


def matrix_divided(matrix, div):
    """
    Divides matrix elements by a given divisor.
    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The divisor.
    Returns:
        New matrix with elements divided by div, rounded to 2 decimal places.
    Raises:
        TypeError if matrix not list of lists of integers/floats or if div not a number (int or float).
    ValueError: If matrix rows not have the same size.
        ZeroDivisionError: If div is 0.

    Example:
        >>> matrix = [
        ...     [1, 2, 3],
        ...     [4, 5, 6]
        ... ]
        >>> matrix_divided(matrix, 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats") 
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = [[round(element / div, 2) for element in row] for row in matrix]
    return result
