#!/usr/bin/python3
"""
rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Args:
      - matrix(List): A list of list to rotate
    """
    len_matrix = len(matrix)
    temp = matrix[::-1]

    for i in range(len_matrix):
        matrix[i] = []
        for j in range(len_matrix):
            matrix[i].append(temp[j].pop(0))
