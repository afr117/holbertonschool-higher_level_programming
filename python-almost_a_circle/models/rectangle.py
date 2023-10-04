# models/rectangle.py
from models.base import Base

class Rectangle(Base):
    """Rectangle class inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.
        
        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): X coordinate of the rectangle's position. Defaults to 0.
            y (int, optional): Y coordinate of the rectangle's position. Defaults to 0.
            id (int, optional): Unique identifier for the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.
        Example: "[Rectangle] (id) x/y - width/height"
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
