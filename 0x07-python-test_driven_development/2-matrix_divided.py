#!/usr/bin/python3
def matrix_divided(matrix, div):
    result = [[round(i / div, 2) for i in row] for row in matrix]
    return (result)