#!/usr/bin/python3
"""Module that defines the is_same_class function."""


def is_same_class(obj, a_class):
    """
    Check if obj is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare obj against.

    Returns:
        True if obj is exactly an instance of a_class; otherwise, False.
    """
    return type(obj) == a_class
