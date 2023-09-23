#!/usr/bin/python3
"""Module to define the Student class."""


class Student:
    """A class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.

        Attributes:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): A list of attribute names to include in the dictionary.
                If provided, only these attributes will be retrieved. Default is None.

        Returns:
            dict: A dictionary containing the specified attributes of the Student.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance using a dictionary.

        Args:
            json (dict): A dictionary containing attribute names and values to replace.
        """
        for key, value in json.items():
            setattr(self, key, value)
