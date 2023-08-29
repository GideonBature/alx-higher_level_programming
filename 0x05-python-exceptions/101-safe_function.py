#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        fct(*args)
        return fct(*args)
    except IndexError as err:
        print("Exception:", err, file=sys.stderr)
        return None
    except ValueError as err:
        print("Exception:", err, file=sys.stderr)
        return None
    except TypeError as err:
        print("Exception:", err, file=sys.stderr)
        return None
    except ZeroDivisionError as err:
        print("Exception:", err, file=sys.stderr)
        return None
