#!/usr/bin/python3
""" Defines a func that prints a square """


def print_square(size):
    """ Prints a square
    Args:
        size (int): the size of square
    Raises:
        TypeError: if size is not an integer
        ValueError: if the size is less than zero
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
