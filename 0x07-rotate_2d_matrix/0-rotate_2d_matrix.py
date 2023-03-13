#!/usr/bin/python3
'''Contains a 2D matrix rotater'''


def rotate_2d_matrix(matrix):
    '''Rotates a 2D matrrix'''
    n = len(matrix)
    matrix_copy = []

    for row in range(n):
        matrix_copy.append([])
        for i in matrix[row]:
            matrix_copy[row].append(i)

    for i in range(n):
        for j in range(n):
            matrix[i][j] = matrix_copy[-j-1][-i-1]

    matrix.reverse()

# Testing infrastructure
# i = 10
# matrix = [[n for n in range(m*i, m*i + i)] for m in range(i)]
# for line in matrix:
#     print(line)

# print('Rotating\n')
# rotate_2d_matrix(matrix)
# for line in matrix:
#     print(line)
