#!/usr/bin/python3
"""
Module for reading text files.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the text file to read.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')

if __name__ == "__main__":
    read_file()
