#!/usr/bin/python3
"""adds all argument to a python list
"""
import sys
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """Adds all arguments to a python list
    and then save them to a file
    """
    filename = "add_item.json"

    if exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    my_list.extend(sys.argv[1:])

    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    main()
