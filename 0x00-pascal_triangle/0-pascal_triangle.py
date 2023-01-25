#!/usr/bin/python3
'''Creates a pascals triangle'''
from math import comb


def expand(n):
    '''Finds the Binominal expansion of n

    Args:
        n (Int): number to be expanded

    Returns:
        List: expansion of n
    '''
    row = []
    i = 0
    while i <= n:
        row.append(comb(n, i))
        i += 1

    return row


def pascal_triangle(n):
    '''Creates a Pascal's triangle

    Args:
        n (Int): number of traiangle rows

    Returns:
        List: nested list representaion of the triangle
    '''
    if n <= 0:
        return []

    triangle = []
    i = 0

    while i < n:
        triangle.append(expand(i))
        i += 1

    return triangle
