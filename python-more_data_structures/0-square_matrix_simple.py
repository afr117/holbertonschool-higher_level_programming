#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix of the same size as the input matrix
    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            # Calculate the square value and append it to the new row
            new_row.append(num ** 2)
        # Append the new row to the new_matrix
        new_matrix.append(new_row)
    return new_matrix
# Example usage
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)
