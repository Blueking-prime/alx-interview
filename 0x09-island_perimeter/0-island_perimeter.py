#!/usr/bin/python3
'''Finds the perimeter of an island'''


def check_surrounding(grid, y, x):
    '''Checks the surrounding of a position to detetermine number of beaches'''
    beach_no = 0
    try:
        if y == 0:
            raise IndexError
        up = grid[y - 1][x]
    except IndexError:
        up = 0
    try:
        down = grid[y + 1][x]
    except IndexError:
        down = 0
    try:
        if x == 0:
            raise IndexError
        left = grid[y][x - 1]
    except IndexError:
        left = 0
    try:
        right = grid[y][x + 1]
    except IndexError:
        right = 0

    if up != 1:
        beach_no += 1
    if down != 1:
        beach_no += 1
    if left != 1:
        beach_no += 1
    if right != 1:
        beach_no += 1

    return beach_no


def island_perimeter(grid):
    '''Calculates the island perimeter'''
    grid_height = len(grid)
    grid_width = len(grid[0])
    beach_no = 0
    for y in range(grid_height):
        for x in range(grid_width):
            if grid[y][x] == 0:
                continue
            beach_no += check_surrounding(grid, y, x)

    return beach_no
