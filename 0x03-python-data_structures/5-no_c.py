#!/usr/bin/python3


def no_c(my_string):
    """ removes c and C from the string """
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return "".join(copy)
