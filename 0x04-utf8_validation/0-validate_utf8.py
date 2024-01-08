#!/usr/bin/python3

"""A method thar determines if a given data is a
valid utf 8 encoding
"""


def validUTF8(data):
    """A function that determines if a given data set represents a
    valid UTF-8 encoding."""
    for char in data:
        binary_rep = bin(char)[2:]
        if check_binary(binary_rep) is False:
            return False
    return True


def check_binary(bin):
    """check the binary representation"""
    length_of_str = len(bin)

    if length_of_str >= 0 and length_of_str <= 8:
        if length_of_str > 7:
            return False
    if length_of_str >= 9 and length_of_str <= 16:
        if length_of_str > 11:
            return False
    if length_of_str >= 17 and length_of_str <= 24:
        if length_of_str > 16:
            return False
    if length_of_str >= 25 and length_of_str <= 32:
        if length_of_str > 21:
            return False
    if length_of_str > 32:
        return False

    return True
