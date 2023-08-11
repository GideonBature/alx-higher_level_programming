#!/usr/bin/python3
def print_argv():
    import sys
    argc = len(sys.argv)
    if argc <= 1:
        print("{:d} arguments.".format(argc - 1))
    elif argc == 2:
        print("{:d} argument:".format(argc - 1))
        print("{:d}: {}".format(argc - 1, sys.argv[1]))
    elif argc > 2:
        print("{:d} arguments:".format(argc - 1))
        for i in range(1, argc):
            print("{:d}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    print_argv()
