#!/usr/bin/python3

'''
A function that returns a list of lists
of integers representing the Pascal’s triangle
of n
'''


def pascal_triangle(n):
    '''
    return the pascal triangle for n
    '''
    if n <= 0:
        return []

    return calc(n)


def calc(n, results=[]):
    '''
    calculate the pascal triangle
    '''
    if (n == 1):
        results.append([1])
        return results
    triangle = calc(n - 1, results)
    new = []
    last = triangle[len(triangle) - 1]
    prev = 0

    for i in last:
        new.append(i + prev)
        prev = i
    new.append(prev)
    results.append(new)
    return results
