#!/usr/bin/python3
"""

Additional comment: This function is a simple example of integer addition.

"""
def add_integer(a, b=98):
    """
    This function adds two integers.
    Args:
        a (int): The first integer.
        b (int, optional): The second integer (default is 98).
    Returns:
        int: The sum of the two integers.
    Raises:
        TypeError: If either 'a' or 'b' is not an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
