#!/usr/bin/python3
"""reads a text file
"""


def read_file(filename=""):
    """Reads file and prints to stdout

    Args:
        filename: name of file to read
    """
    with open(filename, "r", encoding="UTF8") as f:
        for line in f:
            print(line, end="")
