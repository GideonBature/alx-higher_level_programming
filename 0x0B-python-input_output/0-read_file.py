#!/usr/bin/python3
"""reads a text file
"""


def read_file(filename=""):
    """Reads file and prints to stdout

    Args:
        filename: name of file to read
    """
    with open(filename, "r", encoding="utf-8") as f:
        file_read = f.read()
        print(file_read)
