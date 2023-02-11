#!/usr/bin/python3'
""" function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """ Definition of function that divides all elements of matrix
    Args:
        matrix (list of list of integers or float) argumet one:
        div (integer or float): argument two
    Raises:
        TypeError: if the content of the matrix is not float or int
        and if each row of the matrix not have the same size
        ZeroDivisionError: if div is zero
    Returns:
        a new matrix with it elements divides
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    msg2 = "Each row of the matrix must have the same size"

    if len(matrix) == 0 or type(matrix) is not list:
        raise TypeError(msg)
    for i in matrix:
        if type(i) is not list or len(i) is 0:
            raise TypeError(msg)
        for ii in i:
            if type(ii) not in [float, int]:
                raise TypeError(msg)
        if len(i) is not len(matrix[0]):
            raise TypeError(msg2)
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    m = matrix
    return list(map(lambda n: list(map(lambda y: round(y / div, 2), n)), m))
