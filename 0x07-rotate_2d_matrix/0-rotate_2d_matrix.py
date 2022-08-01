#!/usr/bin/python3
"""
 Rotate 2D Matrix
"""


def reverse_row(target, elem):
    """
    Reverse a given row of a matrix
    """
    ans = []
    for i in range(-1, 2):
        if i == 0:
            i = 1
        elif i == 1:
            i = 0
        ans.append(target[i][elem])
    return ans


def fill_matrix(matrix, *argv):
    """
    Fill a matrix with numbers
    """
    matrix.clear()
    for i in range(len(argv)):
        matrix.append(argv[i])


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    """
    if not len(matrix) or len(matrix) != len(matrix[0]):
        return
    top = reverse_row(matrix, 0)
    middle = reverse_row(matrix, 1)
    bottom = reverse_row(matrix, 2)
    fill_matrix(matrix, top, middle, bottom)
