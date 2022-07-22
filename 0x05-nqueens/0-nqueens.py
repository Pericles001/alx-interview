#!/usr/bin/python3
"""
N queens
"""

import sys

if len(sys.argv) != 2:
    print('Usage: nqueens N\n')
    exit(1)

try:
    n_q = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    exit(1)

if n_q < 4:
    print('N must be at least 4')
    exit(1)


def attack_queen(square, queen):
    """
    attack queen method
    """
    (row1, col1) = square
    (row2, col2) = queen
    return (row1 == row2) or (col1 == col2) or\
    abs(row1 - row2) == abs(col1 - col2)

def safe_queen(square, queens):
    """
    Safe queen method
    """
    for queen in queens:
        if attack_queen(square, queen):
            return False
        return True

