#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    num_of_args = len(argv)
    print("{} ".format(num_of_args - 1), end="")
    if num_of_args == 1:
        print("arguments.")
    else:
        if num_of_args == 2:
            print("argument:")
        else:
            print("arguments:")
        for i in range(1, num_of_args):
            print("{}: {}".format(i, argv[i]))
