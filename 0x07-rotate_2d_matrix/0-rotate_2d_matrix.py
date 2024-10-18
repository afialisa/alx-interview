#!/usr/bin/python3
"""2D matrix rotation module.
"""

def rotate_2d_matrix(matrix):
    """Rotates an n by n 2D matrix in place.
    """
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()



