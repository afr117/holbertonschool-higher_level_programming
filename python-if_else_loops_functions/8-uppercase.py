#!/usr/bin/python3

def uppercase(str):
    """Print a string in uppercase followed by a new line"""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print()
