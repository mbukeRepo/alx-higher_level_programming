#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    to_append = 0
    new_list = list([])
    for i in range(list_length):
        try:
            to_append = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            print("wrong type")
            to_append = 0
        except ZeroDivisionError:
            print("division by 0")
            to_append = 0
        except IndexError:
            print("out of range")
            to_append = 0
        finally:
            new_list.append(to_append)
    return (new_list)
