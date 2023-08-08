#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"
str1 = "and is greater than 5"
str2 = "and is less than 6 and not 0"
if number == 0:
    print(f"{str} {number:d} is {number:d} and is 0")
if number < 0:
    number = -number
    last_number = -(number % 10)
    number = -number
    if last_number > 5:
        print(f"{str} {number:d} is {last_number} {str1}")
    elif last_number == 0:
        print(f"{str} {number:d} is {last_number} and is 0")
    elif last_number < 6 and last_number != 0:
        print(f"{str} {number:d} is {last_number} {str2}")

elif number > 0:
    last_number = number % 10
    if last_number > 5:
        print(f"{str} {number:d} is {last_number} {str1}")
    elif last_number == 0:
        print(f"{str} {number:d} is {last_number} and is 0")
    elif last_number < 6 and last_number != 0:
        print(f"{str} {number:d} is {last_number} {str2}")
