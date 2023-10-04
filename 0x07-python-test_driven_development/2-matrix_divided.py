#!/usr/bin/python3
import doctest
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
    result = [[round(i / div, 2) for i in row] for row in matrix]
    return (result)


if __name__ == "__main__":
    doctest.testmod()
