#!/usr/bin/python3
'''Shows possible arrangements of n-queens on a chess board'''
import sys


class mylist (list):
    '''Overwrites default list to prevent negative indexing'''
    def __getitem__(self, n):
        if n < 0:
            raise IndexError("...")
        return list.__getitem__(self, n)


n = 0
grid = mylist()
out_list = set()
out_list_set = set()


def fill_grid(n):
    '''Creates an n x n grid'''
    global grid
    for y in range(n):
        grid.append(mylist())
        for x in range(n):
            grid[y].append(0)


def compile_matrix_output():
    '''Prints out the positions of the queens'''
    global out_list
    out_list = set()
    for y in range(n):
        for x in range(n):
            if grid[y][x]:
                out_list.add((y, x))


def possible(y, x):
    '''Checks if a queen can be placed in this position'''
    # Checks if there's a queen in the row
    for i in range(n):
        if grid[y][i]:
            return False
    # Checks if there's a queen in the column
    for i in range(n):
        if grid[i][x]:
            return False
    # Checks if there's a queen in the diagonal
    for i in range(n):
        try:
            if grid[y - i][x - i]:
                return False
        except IndexError:
            pass
        try:
            if grid[y - i][x + i]:
                return False
        except IndexError:
            pass
        try:
            if grid[y + i][x - i]:
                return False
        except IndexError:
            pass
        try:
            if grid[y + i][x + i]:
                return False
        except IndexError:
            pass
    return True


def count_n():
    count = 0
    for i in grid:
        for j in i:
            if j:
                count += 1
    return count


def solve():
    '''Solves for each position in the board'''
    global grid, out_list, out_list_set
    if count_n() == n:
        compile_matrix_output()
        out_list_set.add(tuple(out_list))
        out_list = set()
    for y in range(n):
        for x in range(n):
            if not grid[y][x]:
                if possible(y, x):
                    grid[y][x] = 1
                    solve()
                    grid[y][x] = 0
                continue


def print_output():
    '''Prints out the output of the program'''
    out_list_list = []
    for i in range(len(out_list_set)):
        out_list_list.append([])

    idx = 0
    for outlist in out_list_set:
        for pair in outlist:
            y, x = pair
            out_list_list[idx].append([y, x])
        idx += 1

    new_out_list_list = []
    for i in out_list_list:
        new_out_list_list.append(sorted(i, key=lambda x: x[0]))
    for i in new_out_list_list:
        print(i)


# Main Code here:
if len(sys.argv) != 2:
    print('Usage: nqueens N')
    sys.exit(1)

try:
    n = int(sys.argv[1])
    if type(n) != int:
        print('N must be a number')
        sys.exit(1)
except Exception:
    print('N must be a number')
    sys.exit(1)

if n < 4:
    print('N must be at least 4')
    sys.exit(1)

fill_grid(n)
solve()
print_output()
