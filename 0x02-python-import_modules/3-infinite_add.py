#!/usr/bin/python3
def print_argv_sum():
    import sys
    num = 0
    argc = len(sys.argv)
    if argc <= 1:
        print("{:d}".format(argc - 1))
    elif argc > 1:
        for i in range(1, argc):
            num += int(sys.argv[i])
        print("{}".format(num))


if __name__ == "__main__":
    print_argv_sum()
