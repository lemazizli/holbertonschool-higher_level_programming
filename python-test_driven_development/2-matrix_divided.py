#!/usr/bin/python3
"""
this module for matrix_divided function. 

It ensures the matrix is valid (list of lists of numbers),
checks if all rows are of equal size, and validates the divisor.
A new matrix is returned with values rounded to two decimal places.
"""


def matrix_divided(matrix, div):
    """
    devides all elements of matrix by a divisor.

    returns : a new matrix containing the results of division.
    """
    msg = "Matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not matrix or not matrix[0]:
        raise TypeError(msg)
    if not isinstance(div, (int, float)):
        raise TypeError("Div must be a number")
    if div == 0:
        raise ZeroDivisionError("Division by zero")
    row_len = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg)
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(msg)
    return [[round(x / div, 2) for x in row] for row in matrix]
