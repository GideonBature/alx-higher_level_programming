#!/usr/bin/python3

def roman_to_int(roman_string):

    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    num = 0;
    prev_num = 0;

    for char in reversed(roman_string):
        value = roman_values[char]
        if value < prev_num:
            num -= value
        else:
            num += value
        prev_num = value

    if num == 0:
        return None
    else:
        return num
