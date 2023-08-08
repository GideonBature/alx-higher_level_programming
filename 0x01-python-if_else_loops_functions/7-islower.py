#!/usr/bin/python3
def islower(c):
    """ checks for lowercase character """
    num_char = ord(c)
    if num_char >= 65 and num_char <= 91:
        return False
    elif num_char >= 97 and num_char <= 123:
        return True
