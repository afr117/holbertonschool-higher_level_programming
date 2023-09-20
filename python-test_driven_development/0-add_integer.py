#!/usr/bin/python3
"""

Additional comment: This function is a simple example of integer addition.

"""
def add_integer(a, b=98):
    """
    Adds two integers.

    :param a: The first integer or float.
    :param b: The second integer or float (default is 98).
    :return: The addition of a and b as an integer.
    """
    # Check if a is an integer or a float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    # Check if b is an integer or a float
    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    # Cast a and b to integers if they are floats
    a = int(a)
    b = int(b)

    # Calculate the sum of a and b
    result = a + b

    return result
