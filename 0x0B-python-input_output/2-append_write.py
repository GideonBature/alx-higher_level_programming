#!/usr/bin/python3
"""appends string to a text file
"""


def append_write(filename="", text=""):
    """Appends strings to text file and returns
    number of characters written

    Args:
        filename: (str) name of file to write to
        text: (str): strings to be written to file

    Return:
        number of characters written
    """
    with open(filename, "a", encoding="UTF8") as f:
        count = f.write(text)
        return count
