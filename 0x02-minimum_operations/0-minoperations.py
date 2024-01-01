#!/usr/bin/python3


"""In a text file, there is a single character H. Your text
editor can execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest number of
operations needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
"""


def get_factors(n):
    """Return a list of tuples for the factors of n"""
    factors = []

    for i in range(1, n + 1):
        if n // i <= 1:
            break
        else:
            if n % i == 0:
                factors.append({
                    "factors": (i, n // i),
                    "sum_factors": i + (n // i)
                })
    return factors


def minOperations(n):
    """Returns the minimum operations needed to result in exactly n H"""
    if n <= 1 or n > 50:
        return 0

    factors = get_factors(n)
    lowest_factor = factors[0]["sum_factors"]

    for factor in factors:
        if factor["sum_factors"] <= lowest_factor:
            lowest_factor = factor["sum_factors"]
    return lowest_factor
