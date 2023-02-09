#!/usr/bin/python3
'''Finds minimum operations to edit a file'''


def minOperations(n):
    '''Finds minimum operations to paste 'H' n times'''
    if n == 1:
        return 0
    if n == 2:
        return 2

    copy = 1
    paste = 1
    h_count = 2
    factor = 2
    check = True

    while n != h_count:
        while n % factor != 0 and n > h_count:
            if check:
                paste += 1
                h_count += 1
                factor += 1
            else:
                paste += 1
                h_count += factor
        check = False

        # checks that factor is a factor of n, factor is not n
        if n % factor == 0 and n != h_count:
            # checks that two times the factor is still a factor of n
            if n % factor * 2 == 0:
                copy += 1
                paste += 1
                factor *= 2
                h_count *= 2

    return copy + paste
