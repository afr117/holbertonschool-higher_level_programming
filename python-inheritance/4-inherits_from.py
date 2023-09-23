#!/usr/bin/python3
"""Module that defines the inherits_from function."""


def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a class that inherited from a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare obj against.

    Returns:
        True if obj is an instance of a class that inherited from a_class; otherwise, False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
