#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = [[x ** 2 for x in y] for y in matrix]
    return square
