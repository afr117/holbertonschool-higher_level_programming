#!/usr/bin/python3
"""
This module defines the Square class.
"""


class Square:
    """
    This is a Square class with a private size attribute.
    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size attribute with type and value validation.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.
        """
        return self.__size * self.__size
