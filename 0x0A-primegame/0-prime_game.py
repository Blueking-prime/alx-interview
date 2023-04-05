#!/usr/bin/python3
'''Find the winner of a prime game'''


def is_prime(i):
    '''Checks if a number is prime'''
    if i == 1:
        return False
    if i == 2 or i == 3 or i == 5 or i == 7:
        return True
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        return False

    factor_list = [j for j in range(i) if is_prime(j)]
    for j in factor_list:
        if i % j == 0:
            return False

    return True


def round_winner(num):
    '''Determines who wins a round'''
    wins = 0
    num_list = list(range(num))
    for i in num_list:
        if is_prime(i):
            wins += 1

    return wins


def isWinner(x, nums):
    '''Determines the winner of the game'''
    i = 0
    b = 0
    m = 0
    if i > len(nums):
        return None

    while i < x:
        if round_winner(nums[i]) % 2 == 0:
            b += 1
        else:
            m += 1
        i += 1

    if b == 0 and m == 0:
        return None

    if b < m:
        return 'Maria'
    else:
        return 'Ben'
