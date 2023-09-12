#!/usr/bin/python3
"""write string to a text file
"""


def write_file(filename="", text=""):
    """Write strings to text file and returns
    number of characters written

    Args:
        filename: (str) name of file to write to
        text: (str): strings to be written to file

    Return:
        number of characters written
    """
    with open(filename, "w", encoding="UTF8") as f:
        count = f.write(text)
        return count
