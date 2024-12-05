#!/usr/bin/python3
"""
Rotate 2D-matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D-matrix 90 degrees clockwise.
    Args:
        matrix (list of lists): the matrix.
    """
    n = len(matrix)
    for i in range(int(n / 2)):
        y = (n - i - 1)
        for j in range(i, y):
            x = (n - 1 - j)
            tmp = matrix[i][j]
            # swap top to left
            matrix[i][j] = matrix[x][i]
            # swap left to down
            matrix[x][i] = matrix[y][x]
            # swap down to right
            matrix[y][x] = matrix[j][y]
            # swap right to top
            matrix[j][y] = tmp
