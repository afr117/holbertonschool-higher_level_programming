#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Extract the first and second elements from each tuple
    a1, a2 = tuple_a + (0, 0)
    b1, b2 = tuple_b + (0, 0)
    # Calculate the sum of the corresponding elements
    sum_1 = a1 + b1
    sum_2 = a2 + b2
    # Return the result as a new tuple
    return (sum_1, sum_2)
