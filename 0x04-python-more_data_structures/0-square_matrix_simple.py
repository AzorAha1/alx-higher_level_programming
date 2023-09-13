#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return matrix
    output = [[i ** 2 for i in row] for row in matrix]
    return output