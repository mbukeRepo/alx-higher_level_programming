#!/usr/bin/python3
""" Defines instance checker """


def is_same_class(obj, a_class):
    """ Returns true if obj is instance of class
    Args:
       obj (any): object to check
       a_class (type): class of object

    """
    if type(obj) != a_class:
        return False
    return True
