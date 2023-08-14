#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """prints all integers of a list"""
    len_num = len(my_list)
    for i in range(0, len_num):
        print("{}".format(my_list[i]))
