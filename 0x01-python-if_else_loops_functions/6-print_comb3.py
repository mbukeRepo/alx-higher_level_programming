#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        if i * 10 + j == 89:
            print("{}{}".format(i, j))
            break
        else:
            print("{}{}".format(i, j), end=", ")
