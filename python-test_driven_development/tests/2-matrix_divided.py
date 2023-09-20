# Test cases for matrix_divided function

>>> matrix = [
...     [1, 2, 3],
...     [4, 5, 6]
... ]
>>> matrix_divided(matrix, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

>>> matrix = [
...     [1, 2, 3],
...     [4, 5, 6]
... ]
>>> matrix_divided(matrix, 0)
ZeroDivisionError: division by zero

>>> matrix = [
...     [1, 2, 3],
...     [4, 5, "six"]
... ]
>>> matrix_divided(matrix, 2)
TypeError: matrix must be a matrix (list of lists) of integers/floats

>>> matrix = [
...     [1, 2, 3],
...     [4, 5, 6, 7]
... ]
>>> matrix_divided(matrix, 2)
ValueError: Each row of the matrix must have the same size

>>> matrix_divided(None, 2)
TypeError: matrix must be a matrix (list of lists) of integers/floats

>>> matrix = [
...     [1, 2, 3],
...     [4, 5, 6]
... ]
>>> matrix_divided(matrix, "two")
TypeError: div must be a number

