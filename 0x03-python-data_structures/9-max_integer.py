#!/usr/bin/python3


def max_integer(my_list=[]):
    largest = my_list[0]
    size = len(my_list)
    if size == 0:
        return None
    for i in range(size):
        if my_list[i] > largest:
            largest = my_list[i]
    return largest
