#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """ deletes the item at a specific position in a list """
    list_len = len(my_list)
    new_list = my_list

    if idx < 0:
        return new_list
    if idx > list_len:
        return new_list
    for item in new_list:
        if idx == item:
            del new_list[idx]
            return new_list
