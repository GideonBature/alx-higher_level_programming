#!/usr/bin/python3
def remove_char_at(str, n):
    """ creates copy of string & remove char @ n """
    if n < 0:
        return str
    else:
        strcpy = str[:n] + str[n + 1:]
        return strcpy
