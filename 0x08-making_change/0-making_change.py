#!/usr/bin/python3
'''Determines fewest coins to create a total'''


def makeChange(coins, total):
    '''Calulates number of coins'''
    if total <= 0:
        return 0

    coins.sort()
    no = 0
    i = len(coins) - 1
    while i > 0:
        if total - coins[i] >= 0:
            no += 1
            total -= coins[i]
        else:
            i -= 1

    if total == 0:
        return no

    return -1
