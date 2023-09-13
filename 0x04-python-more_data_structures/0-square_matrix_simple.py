#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    output = []
    for row in matrix:
        innermat = []
        for eachvalue in row:
            squareeachvalue = eachvalue ** 2
            innermat.append(squareeachvalue)
            output.append(innermat)
        return output
