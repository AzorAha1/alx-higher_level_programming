#!/usr/bin/python3
def matrix_divided(matrix, div):
    result = [[i / div for i in row] for row in matrix]
    return result