#!/usr/bin/python3

"""A method thar determines if a given data is a
valid utf 8 encoding
"""


def validUTF8(data):
    """A function that determines if a given data set represents a
    valid UTF-8 encoding."""
    next_bytes_to_check = 0
    for single_data in data:
        binary_rep = bin(single_data)[2:].zfill(8)
        if next_bytes_to_check == 0:
            if binary_rep.startswith("0"):
                continue
            elif binary_rep.startswith("110"):
                next_bytes_to_check = 1
            elif binary_rep.startswith("1110"):
                next_bytes_to_check = 2
            elif binary_rep.startswith("11110"):
                next_bytes_to_check = 3
            else:
                return False
        else:
            if binary_rep.startswith("10"):
                next_bytes_to_check -= 1
            else:
                return False

    return next_bytes_to_check == 0
