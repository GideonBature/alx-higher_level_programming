#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """ retrieves an element from a list like C """
    len_list = len(my_list)
    if idx < 0:
        return my_list
    elif idx > len_list - 1:
        return my_list
    else:
        for num in my_list:
            if idx == num - 1:
                my_new_list = my_list.copy()
                my_new_list[idx] = element
                return my_new_list
