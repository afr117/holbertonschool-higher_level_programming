#!/usr/bin/python3
"""

Additional comment: This function is a simple example of integer addition.

"""
def add_integer(a, b=98):
    """
    Args: a (int or float): The first integer or float: b (int or float, optional): Second integer or float (default 98).
    Returns:
        int: The addition of 'a' and 'b' as integers
    Raises:
        TypeError: If 'a' or 'b' is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
