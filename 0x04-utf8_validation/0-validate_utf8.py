#!/usr/bin/python3
'''Decodes a utf-8 string'''


def validASCII(data):
    '''Checks if data is a valid utf-8 character'''
    try:
        bin_list = []
        for i in data:
            bin_list.append(i.to_bytes())

        return True
    except OverflowError:
        return False


def check_lead(test):
    '''Checks leading byte to determine code point length'''
    if int(test) in range(0, 128):
        return 1
    if int(test) in range(194, 224):
        return 2
    if int(test) in range(224, 240):
        return 3
    if int(test) in range(240, 248):
        return 4
    return None


def convert_to_string(code_point):
    '''Converts code point to utf-8 string'''
    return chr(code_point)


def validUTF8(data):
    '''Checks if data is valid in UTF-8'''
    for i in range(len(data)):
        check = check_lead(data[i])
        try:
            if check == 1:
                convert_to_string(data[i])
                i += 1
                continue
            elif check == 2:
                l_byte = (data[i] - 194) * 64
                t_byte_1 = data[i + 1] - 128
                code_point = l_byte + t_byte_1
                convert_to_string(code_point)
                i += 2
                continue
            elif check == 3:
                l_byte = (data[i] - 224) * 4096
                t_byte_1 = (data[i + 1] - 128) * 64
                t_byte_2 = data[i + 2] - 128
                code_point = l_byte + t_byte_1 + t_byte_2
                convert_to_string(code_point)
                i += 3
                continue
            elif check == 4:
                l_byte = (data[i] - 240) * 262144
                t_byte_1 = (data[i + 1] - 128) * 4096
                t_byte_2 = (data[i + 2] - 128) * 64
                t_byte_3 = data[i + 3] - 128
                code_point = l_byte + t_byte_1 + t_byte_2 + t_byte_3
                convert_to_string(code_point)
                i += 4
                continue
            else:
                return False
        except Exception:
            return False

    return True
