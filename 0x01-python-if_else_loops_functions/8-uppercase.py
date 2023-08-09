#!/usr/bin/python3
def uppercase(str):
    """ prints a string in uppercase """
    for s in str:
        num_char = ord(s)
        if num_char >= 97 and num_char <= 123:
            num_char -= 32
        elif num_char >= 65 and num_char <= 90 or num_char == 32:
            num_char = num_char
        char = chr(num_char)
        print("{}".format(char), end="")
    print()
