#!/usr/bin/python3
""" Defines square class """


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Represents Square class """
    def __init__(self, size):
        """ class constructor
        Args:
           size (int): size of the square
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ Returns area of square """
        return self.__size * self.__size

    def __str__(self):
        """ representation implementation """
        return "[Square] {}/{}".format(self.__size, self.__size)
