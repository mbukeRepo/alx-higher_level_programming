#!/usr/bin/python3
""" Define a square class """


class Square:
    """ Represents a Square """
    def __init__(self, size=0):
        """ Initialises new Square

        Args:
            size (int): size of side of the square
        """
        if not isinstance(self, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
