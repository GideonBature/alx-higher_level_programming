#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """prints all integers of a list"""
    for num in my_list:
        f_str = "{}"
        result = f_str.format(my_list[num - 1])
        print(result)
