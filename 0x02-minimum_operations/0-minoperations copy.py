#!/usr/bin/python3
'''Finds minimum operations to edit a file'''
from time import sleep


def minOperations(n: int) -> int:
    '''Finds minimum operations to paste 'H' n times'''
    if n == 1:
        return 0
    if n == 2:
        return 2

    print(1)
    copy: int = 1
    print('c')
    paste: int = 1
    print('p')
    h_count = 2
    print(h_count)
    factor = 2
    check = True

    while n != h_count:
        while n % factor != 0 and n > h_count:
            if check:
                paste += 1
                print('p')
                h_count += 1
                print(h_count)
                factor += 1
                sleep(0.5)
            else:
                paste += 1
                print('p')
                print('factor:', factor)
                h_count += factor
                print(h_count)
                sleep(0.5)
        check = False

        # checks that factor is a factor of n, factor is not n
        if n % factor == 0 and n != h_count:
            # checks that two times the factor is still a factor of n
            if n % factor * 2 == 0:
                copy += 1
                print('c')
                paste += 1
                print('p')
                factor *= 2
                print('factor:', factor)
                h_count *= 2
                print(h_count)

    return copy + paste


n = 3
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 8
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 9
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
