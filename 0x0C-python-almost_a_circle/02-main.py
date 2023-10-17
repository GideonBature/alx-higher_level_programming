#!/usr/bin/python3
""" Check """
from models.rectangle import Rectangle

try:
    Rectangle("12", 13)
    print("TypeError exception not raised")
except TypeError as e:
    if str(e) != "width must be an integer":
        print("Wrong exception message: {}".format(e))
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))

try:
    Rectangle([13], 13)
    print("TypeError exception not raised")
except TypeError as e:
    if str(e) != "width must be an integer":
        print("Wrong exception message: {}".format(e))
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))

try:
    Rectangle(13.12, 13)
    print("TypeError exception not raised")
except TypeError as e:
    if str(e) != "width must be an integer":
        print("Wrong exception message: {}".format(e))
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))

try:
    Rectangle({ 'id': 12 }, 13)
    print("TypeError exception not raised")
except TypeError as e:
    if str(e) != "width must be an integer":
        print("Wrong exception message: {}".format(e))
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))

print("OK", end="")
