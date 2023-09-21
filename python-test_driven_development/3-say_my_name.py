#!/usr/bin/python3
"""
test
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>."

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name.

    Raises:
        TypeError: If first_name or last_name is not a string.

    Example:
        >>> say_my_name("John", "Smith")
        My name is John Smith.
        >>> say_my_name("Walter", "White")
        My name is Walter White.
        >>> say_my_name("Bob")
        My name is Bob.
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {} ".format(first_name))

if __name__ == "__main__":
    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")
    try:
        say_my_name(12, "White")
    except Exception as e:
        print(e)
