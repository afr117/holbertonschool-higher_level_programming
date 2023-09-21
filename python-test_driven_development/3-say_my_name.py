#!/usr/bin/python3
"""
test
"""


def say_my_name(first_name, last_name=""):
    """
Prints 'My name is <first name> <last name>.'
Args:
    first_name (str): The first name.
    last_name (str, optional): The last name.
Raises TypeError if first_name or last_name not provided as strings.
Examples:
    >>> say_my_name('John', 'Smith')
    My name is John Smith.
    >>> say_my_name('Walter', 'White')
    My name is Walter White.
    >>> say_my_name('Bob')
    My name is Bob.
"""
    if not isinstance(first_name, str) or not (isinstance(last_name, str) if last_name else True):
        raise TypeError("first_name must be a string" if not isinstance(first_name, str) else "last_name must be a string")
    
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is { }.".format(first_name))
