#!/usr/bin/python3
"""function
"""


def pascal_triangle(n):
    """pascal_triangle
    """
    thelist = []
    for i in range(n):
        inner_list = []
        for j in range(i + 1):
            if j == 0 or j == i:
                inner_list.append(1)
            else:
                inner_list.append(thelist[i - 1][j - 1] + thelist[i - 1][j])
        thelist.append(inner_list)
    return thelist
