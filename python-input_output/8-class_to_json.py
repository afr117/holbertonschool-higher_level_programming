#!/usr/bin/python3
"""
Module for converting a class object to a JSON serializable dictionary.
"""

def class_to_json(obj):
    """
    Converts a class object to a JSON serializable dictionary.

    Args:
        obj: The instance of a class to be converted.

    Returns:
        dict: A dictionary representation of the class object.
    """
    return obj.__dict__
