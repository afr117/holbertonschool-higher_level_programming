#!/usr/bin/python3

class Base:
    """Base class for geometric shapes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance with an optional ID."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
