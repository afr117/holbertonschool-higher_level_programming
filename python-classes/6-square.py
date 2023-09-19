#!/usr/bin/python3
"""
This module defines the Square class.
"""


class Square:
    """
    This is a Square class with private size and position attributes.
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieve the position attribute.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position attribute with type and value validation.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(val, int) for val in value) or \
           not all(val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square with '#' characters and position.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
