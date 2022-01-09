#!/usr/bin/python3
""" Defines a method that finds the peak """


def find_peak(list_of_integers):
    """
      finds peak in a list
      Args:
        list_of_integers (list): list of numbers
    """
    if list_of_integers == []:
        return None

    ln = len(list_of_integers)

    if ln == 1:
        return list_of_integers[0]

    if ln == 2:
        return max(list_of_integers)

    mid = int(ln / 2)

    pk = list_of_integers[mid]

    if pk > list_of_integers[mid - 1] and pk > list_of_integers[mid + 1]:
        return pk
    elif pk < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
