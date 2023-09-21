#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>."

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name.

    Raises:
        TypeError: If first_name is not a string or if last_name is provided and is not a string.

    Example:
        >>> say_my_name("John", "Smith")
        My name is John Smith.
        >>> say_my_name("Walter", "White")
        My name is Walter White.
        >>> say_my_name("Bob")
        My name is Bob.
    """
    if not isinstance(first_name, str) or (last_name and not isinstance(last_name, str)):
        raise TypeError("first_name must be a string" if not isinstance(first_name, str) else "last_name must be a string")
    if last_name:
        print("My name is {} {}.".format(first_name, last_name))
    else:
        print("My name is {} ".format(first_name))

