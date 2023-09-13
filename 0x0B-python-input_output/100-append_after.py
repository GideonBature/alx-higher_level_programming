#!/usr/bin/python3
"""Search and update
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert after each matching line.
    """
    modified_lines = []

    with open(filename, 'r') as file:
        lines = file.readlines()

        for line in lines:
            modified_lines.append(line)

            if search_string in line:
                modified_lines.append(new_string)

    with open(filename, 'w') as file:
        file.writelines(modified_lines)
