#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """prints all integers of a list"""
    len_num = len(my_list)
    for i in range(0, len_num):
        f_str = "{}"
        result = f_str.format(my_list[i])
        print(result)
