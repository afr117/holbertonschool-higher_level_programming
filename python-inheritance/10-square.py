#!/usr/bin/python3
"""Module that defines the Square class."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, size):
        """Initialize a Square instance with size."""
        self.integer_validator("size", size)
        super().__init__(size, size)  # Call the constructor of the base class

    def __str__(self):
        """Return a string representation of the Square."""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
