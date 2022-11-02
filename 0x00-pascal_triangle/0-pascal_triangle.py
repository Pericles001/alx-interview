#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
         returns a list of lists of
         integers representing
          the Pascal’s triangle of n
         Returns an empty list if n <= 0
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(n - 1):
        triangle.append([1] + [triangle[i][j] + triangle[i][j + 1]
                               for j in range(i)] + [1])
    return triangle
