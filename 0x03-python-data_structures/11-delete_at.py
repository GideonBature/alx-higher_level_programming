#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """ deletes the item at a specific position in a list """
    list_len = len(my_list)

    if idx < 0:
        return my_list
    if idx > list_len - 1:
        return my_list
    for item in my_list:
        if idx == item - 1:
            del my_list[idx]
            return my_list
