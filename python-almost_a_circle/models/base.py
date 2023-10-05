#!/usr/bin/python3
"""
Base module - Contains the Base class
"""

import json


class Base:
    """Base class for managing instances."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new Base instance.

        Args:
            id (int, optional): Unique identifier for instance.Defaults None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list dict):List dictionary to convert to JSON.

        Returns:
            str: JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
