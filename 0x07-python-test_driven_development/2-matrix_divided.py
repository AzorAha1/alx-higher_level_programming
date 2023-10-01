import doctest
#!/usr/bin/python3
def matrix_divided(matrix, div):
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = [[round(i / div, 2) for i in row] for row in matrix]
    return (result)
if __name__ == "__main__":
    doctest.testmod()
