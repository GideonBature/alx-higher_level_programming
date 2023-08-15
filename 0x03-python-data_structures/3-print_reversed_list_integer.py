#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_len = len(my_list)

    if list_len == 0:
        return
    else:
        reversed_list = my_list
        reversed_list.reverse()

        for num in reversed_list:
            print("{:d}".format(num))
