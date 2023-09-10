#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Use indexing to access elements or use 0 for missing elements
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0
    
    # Calculate the sums
    sum1 = a1 + b1
    sum2 = a2 + b2
    
    # Return a tuple with the sums
    return (sum1, sum2)
