#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """ Prints x elements of list
        Args:
          my_list (list): list of elements to print
          x (int): number of elements to print
    """
    ret = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            pass
    print("")
    return (ret)
