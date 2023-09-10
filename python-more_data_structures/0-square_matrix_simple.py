#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Find all integers in the matrix
    integers = set()
    for row in matrix:
        integers.update(set(filter(lambda x: isinstance(x, int), row)))

    # Square the integers and create a new matrix
    new_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            if item in integers:
                new_row.append(item ** 2)
            else:
                new_row.append(item)
        new_matrix.append(new_row)

    return new_matrix
