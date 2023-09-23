#!/usr/bin/python3
"""
Module that defines the is_kind_of_class function.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if obj is an instance of, or inherited from, the specified class.
    Args:
        obj: The object to check.
        a_class: The class to compare obj against.

    Returns:
        True if obj is an instance of, or inherited from, a_class; otherwise, False.
    """
    return isinstance(obj, a_class)
