#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperation').minOperations

n = 2147483640
# n = 972
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))