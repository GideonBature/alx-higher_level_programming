#!/usr/bin/python3
def element_at(my_list, idx):
    """ retrieves an element from a list like C """
    len_list = len(my_list)
    if idx < 0:
        return None
    elif idx > len_list - 1:
        return None
    else:
        for num in my_list:
            if idx == num - 1:
                return my_list[idx]
