#!/usr/bin/python3


def safe_print_integer(value):
    """ prints value passed in
        Args:
          value (int): integer to print
        Return:
          True for successful printing or false for failure to print
    """
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        return (False)
    else:
        return (True)
