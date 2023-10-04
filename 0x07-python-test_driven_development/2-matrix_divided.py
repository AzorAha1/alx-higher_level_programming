#!/usr/bin/python3
"""function to divide matrix
    this divides elements in a matrix
"""


def matrix_divided(matrix, div):
    """matrix_divided
        matrix = the matrix
        div = what we are divided every element with
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if not all(isinstance(r, list) and
               all(isinstance(e, (float, int))for e in r)for r in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    result = [[round(i / div, 2) for i in row] for row in matrix]
    return (result)
