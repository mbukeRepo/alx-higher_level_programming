#!/usr/bin/python3
""" Defines Rectangle class """

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Represents Rectangle class """
    def __init__(self, width, height):
        """ class constructor
        Args:
           width (int): width of the rectangle
           height (int): height of the rectangle
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
