#!/usr/bin/python3
import sys
zero = 0
argv_count = len(sys.argv) - 1
argv_count_range = len(sys.argv)
if len(sys.argv) == 1:
    print("{:d} arguments.".format(zero))
elif len(sys.argv) > 1:
    print("{:d} arguments:".format(argv_count))
    for i in range(1, argv_count_range):
        print("{:d}: {}".format(i, sys.argv[i]))
