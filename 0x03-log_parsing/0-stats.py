#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""

import sys
import re

count = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
file_size = 0

try:
    for user_input in sys.stdin:
        tokens = user_input.split(" ")
        matches = len(tokens) > 4

        if matches:
            status_code = tokens[-2]
            if status_code in status_codes.keys():
                status_codes[status_code] = status_codes[status_code] + 1
            file_size = file_size + int(tokens[-1])

            count = count + 1

        if (count == 10):
            print("File size: {}".format(file_size))
            for key, val in status_codes.items():
                if (val > 0):
                    print("{}: {}".format(key, val))
            count = 0
except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(file_size))
    for key, val in sorted(status_codes.items()):
        if (val > 0):
            print("{}: {}".format(key, val))
    count = 0
