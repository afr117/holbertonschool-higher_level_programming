#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_str = ""
        for i, num in enumerate(row):
            row_str += "{:d}".format(num)
            if i < len(row) - 1:
                row_str += " "
        row_str += "$"
        print(row_str)

# Example usage
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print_matrix_integer(matrix)

