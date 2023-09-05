#!/usr/bin/python3
"""LockedClass with no class or object attribute
"""


class LockedClass:
    """No class or object attribute
    """
    def __setattr__(self, name, value):
        """Set attribute if attribute is first_name
        """
        if name == 'first_name':
            self.__dict__[name] = value
        else:
            raise AttributeError("'LockedClass' object has no attribute 'last_name'")
