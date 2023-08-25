#!/usr/bin/python3

def roman_to_int(roman_string):

    if not isinstance(roman_string, str):
        return 0
    if roman_string is None:
        return 0

    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    num = 0
    prev_num = 0

    for char in reversed(roman_string):
        value = val[char]
        if value < prev_num:
            num -= value
        else:
            num += value
        prev_num = value

    return num
