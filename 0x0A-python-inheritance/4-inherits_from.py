#!/usr/bin/python3
""" Defines checker for inherited class of object """


def inherits_from(obj, a_class):
    """ Returns true if obj is instance of inherited class from a_class
    Args:
       obj (any): object
       a_class (type): base class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
