#!/usr/bin/python3
""" Defines a printing function """


def say_my_name(first_name, last_name=""):
    """ Prints firstname and last name
    Args:
        first_name (str): first arg
        last_name (str): second arg
    Raises:
        TypeError: if first name or last name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
