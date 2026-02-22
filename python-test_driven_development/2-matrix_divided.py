#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
The matrix must be a list of lists of integers or floats.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): The number to divide the matrix by.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.

    Returns:
        list: A new matrix with the results.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or not matrix or not matrix[0]:
        raise TypeError(msg)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg)
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(msg)

    row_len = len(matrix[0])

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    return [[round(x / div, 2) for x in row] for row in matrix]
