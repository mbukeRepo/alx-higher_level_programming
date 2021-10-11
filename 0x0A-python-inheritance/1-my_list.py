#!/usr/bin/python3
""" Defines a class that extends native list"""


class MyList(list):
    """ Represents a custom list """
    def print_sorted(self):
        """ prints a sorted list """
        print(sorted(self))
