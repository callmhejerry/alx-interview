#!/usr/bin/python3

"""A method thar determines if a given data is a
valid utf 8 encoding
"""


def validUTF8(data):
    """A function that determines if a given data set represents a
    valid UTF-8 encoding."""
    for char in data:
        binary_rep = bin(char)[2:]
        if len(binary_rep) >= 8:
            return False

    return True
