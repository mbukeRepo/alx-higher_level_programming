#!/usr/bin/python3
""" Defines integer addition of two integers"""


def add_integer(a, b=98):
    """Returns the addition of a and b
    Args:
       a(int) : first number
       b(int) : second number
    Raises:
       TypeError: if a or b are not integers
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
