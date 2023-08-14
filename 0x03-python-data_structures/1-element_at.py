#!/usr/bin/python3
def element_at(my_list, idx):
    """ retrieves an element from a list like C """
    len_list = len(my_list)
    if idx < 0:
        return None
    if idx > len_list:
        return None
    for num in my_list:
        if num == idx:
            return my_list[idx]
