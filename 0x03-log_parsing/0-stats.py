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
        if (count == 10):
            print("File size: {}".format(file_size))
            for key, val in status_codes.items():
                if (val > 0):
                    print("{}: {}".format(key, val))
            count = 0
        else:
            pattern = r'\b(\d{3})\s(\d+)\b'
            matches = re.search(pattern, user_input)

            if matches:
                status_code = matches.group(1)

                status_codes[status_code] = status_codes[status_code] + 1
                file_size = file_size + int(matches.group(2))

            count = count + 1
except KeyboardInterrupt:
    print("File Size: {}".format(file_size))
    for key, val in status_codes.items():
        if (val > 0):
            print("{}: {}".format(key, val))
    count = 0
