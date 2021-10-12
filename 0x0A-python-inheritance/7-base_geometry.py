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
    
    def integer_validator(self, name, value):
        """ Validates value for name
        Args:
          name (str): name of object to be validated
          value (int): value to be validated
        Raises:
          TypeError: if value is not an int
          ValueError: if value is less than zero
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be greater than 0".format(name))

