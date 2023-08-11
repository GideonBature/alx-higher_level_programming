#!/usr/bin/python3
import hidden_4


def print_names():
    names = dir(hidden_4)
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)


if __name__ == "__main__":
    print_names()
