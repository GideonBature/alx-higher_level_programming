#!/usr/bin/python3
"""a class MyList that inherits from list
"""


class MyList(list):
    """class that inherits from list

    Args:
        list - argument
    """
    def print_sorted(self):
        """print list in sorted order
        """
        print(sorted(self))
