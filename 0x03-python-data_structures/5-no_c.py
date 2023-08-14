#!/usr/bin/python3
def no_c(my_string):
    """ removes all characters c and C from a string """
    new_string = my_string.replace('c', "")
    new_str = new_string.replace('C', "")
    return new_str
