#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return matrix
    mat = []
    for row in matrix:
        mat.append(list(map(lambda i : i ** 2, row)))
    return mat