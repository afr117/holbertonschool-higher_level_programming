#!/usr/bin/python3
"""
This module defines a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Add two integers.

    :param a: The first integer.
    :param b: The second integer (default is 98).
    :type a: int
    :type b: int
    :return: The sum of a and b.
    :rtype: int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
