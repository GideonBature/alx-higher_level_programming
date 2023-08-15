#!/usr/bin/python3
def max_integer(my_list=[]):
    """ finds the biggest integer of a list """
    int_len = len(my_list)
    if int_len == 0:
        return None
    else:
        my_list.sort(reverse=True)
        return my_list[0]
