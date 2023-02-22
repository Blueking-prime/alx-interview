#!/usr/bin/python3
'''Decodes a utf-8 string'''


def validASCII(data: list[int]):
    '''Checks if data is a valid utf-8 character'''
    try:
        bin_list = []
        for i in data:
            bin_list.append(i.to_bytes())

        return True
    except OverflowError:
        return False


def validUTF8(data):
    '''Checks if data is valid in UTF-8'''
    return validASCII(data)
