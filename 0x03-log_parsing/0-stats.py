#!/usr/bin/python3
'''reads stdin line by line and computes metrics'''
import sys, re


with sys.stdin as input_stream:
    total_size = 0
    code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    try:
        line_count = 0
        for line in input_stream: # Reads through input stream line by line
            compare_string = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d\d-\d\d \d\d:\d\d:\d\d.\d{6}\] "GET /projects/260 HTTP/1.1" \d{3} \d{1,4}')
            reg_search = compare_string.search(line)
            if reg_search:
                file_size_reg_match = re.compile(r'HTTP/1.1" (\d{3}) (\d{1,4})')
                rty = file_size_reg_match.search(line)
                status_code, file_size = rty.groups() # type: ignore
                try:
                    file_size = int(file_size)
                    total_size += file_size

                    status_code = int(status_code)
                    if status_code in code_count:
                        code_count[status_code] += 1
                except ValueError:
                    pass
                line_count += 1
                if line_count == 10:
                    line_count = 0
                    print('File size: {}'.format(total_size))
                    for i in code_count:
                        if code_count[i]:
                            print('{}: {}'.format(i, code_count[i]))
    except KeyboardInterrupt:
        print('File size: {}'.format(total_size))
        for i in code_count:
            if code_count[i]:
                print('{}: {}'.format(i, code_count[i]))
