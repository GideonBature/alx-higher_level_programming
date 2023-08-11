#!/usr/bin/python3
import sys
argv_count = len(sys.argv) - 1
argv_count_range = len(sys.argv)
if len(sys.argv) == 1:
    print(f"{0:d} arguments.")
elif len(sys.argv) > 1:
    print(f"{argv_count:d} arguments:")
    for i in range(1, argv_count_range):
        print(f"{i}: {sys.argv[i]}")
