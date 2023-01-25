#!/usr/bin/python3
'''Creates a pascals triangle'''


def f(n):
    '''Find the factorial of n'''
    if n == 0 or n == 1:
        return 1

    return n * f(n - 1)


def expand(n):
    '''Finds the Binominal expansion of n

    Args:
        n (int): number to be expanded

    Returns:
        List: expansion of n
    '''
    row = []
    i = 0
    while i <= n:
        row.append(int(f(n) / (f(i) * f(n - i))))
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
        return [[]]

    triangle = []
    i = 0

    while i < n:
        triangle.append(expand(i))
        i += 1

    return triangle
