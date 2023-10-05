#!/usr/bin/python3
"""
Square module - Contains the Square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle class.

    Attributes:
        size (int): Size of the square.
        x (int): X coordinate of the square's position.
        y (int): Y coordinate of the square's position.
        id (int): Unique identifier for the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): Size of square.
            x (int,optional): X coordinate of square position. Default 0.
            y (int,optional): Y coordinate of square position. Default 0.
            id (int,optional): Unique identifier for square. Default None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation of Square."""
        return "[Square]({}){}/{}-{}".format(
                self.id, self.x, self.y, self.width
                )

    @property
    def size(self):
        """Getter for size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size attribute."""
        self.width = value
        self.height = value

    def area(self):
        """Returns the area of the square."""
        return self.width * self.height
