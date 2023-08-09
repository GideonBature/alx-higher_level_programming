#!/usr/bin/python3
for i in range(122, 90, -1):
    if i >= 91 and i <= 96:
        continue
    if i % 2 == 0:
        i = i
    elif i % 2 == 1:
        i -= 32
    print("{}".format(chr(i)), end="")
