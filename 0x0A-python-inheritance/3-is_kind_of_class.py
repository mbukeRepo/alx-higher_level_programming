#!/usr/bin/python3
""" Defines instance checker"""


def is_kind_of_class(obj, a_class):
    """ Returns true if obj is instance of a_class
    Args:
       obj (any): object
       a_class (type): class
    """
    if isinstance(obj, a_class):
        return True
    return False
