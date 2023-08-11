#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def calc():
    import sys
    argc = len(sys.argv)
    if (argc - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        op = sys.argv[2]
        b = int(sys.argv[3])
        if op == '+':
            print("{:d} {} {:d} = {:d}".format(a, op, b, add(a, b)))
        elif op == '-':
            print("{:d} {} {:d} = {:d}".format(a, op, b, sub(a, b)))
        elif op == '*':
            print("{:d} {} {:d} = {:d}".format(a, op, b, mul(a, b)))
        elif op == '/':
            print("{:d} {} {:d} = {:d}".format(a, op, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)


if __name__ == "__main__":
    calc()
