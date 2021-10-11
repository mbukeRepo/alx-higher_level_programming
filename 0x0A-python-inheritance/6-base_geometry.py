#!/usr/bin/python3
""" Defines BaseGeometry class"""


class BaseGeometry:
    """ Base Geometry """
    def area(self):
        """ area of shape
        Raises:
            Exception: default
        """
        raise Exception("area() is not implemented")
