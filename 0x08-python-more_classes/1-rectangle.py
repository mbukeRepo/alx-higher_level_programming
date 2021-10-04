#!/usr/bin/python3
""" Defines Rectangle class """


class Rectangle:
    """ Represents a rectangle. """
    def __init__(self, width=0, height=0):
        """ initialises new Rectangle
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Get/set width of the triangle """
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise(TypeError("width must be an integer"))
        elif width < 0:
            raise(ValueError("width must be >= 0"))
        else:
            self.__width = width

    @property
    def height(self):
        """ Get/Set height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise(TypeError("height must be an integer"))
        elif height < 0:
            raise(ValueError("height must be >= 0"))
        else:
            self.__height = height
