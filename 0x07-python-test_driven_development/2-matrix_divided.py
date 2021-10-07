#!/usr/bin/python3
""" Defines a function that divides the matrix elements with div """


def matrix_divided(matrix, div):
    """ Returns new matrix with quotients
    Args:
        matrix (list): multi-dimension list of numbers
        div (int): number to divide matrix elements with
    Raises:
        TypeError: when rows are not equal and elements not float/integer
        ZeroDivisionError: if the div is zero
    """
    # dealing with div
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    #dealing with matrix
    
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(num, int) or isinstance(num, float)
                for num in [el for row in matrix for el in row])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
