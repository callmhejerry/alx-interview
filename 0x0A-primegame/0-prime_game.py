#!/usr/bin/python3
"""Program that performs prime game"""


def isWinner(x, nums):
    """Function that performs prime game"""
    if not nums or x < 1:
        return None
    n = max(nums)
    filteredList = [True for _ in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not filteredList[i]:
            continue
        for j in range(i * i, n + 1, i):
            filteredList[j] = False
    filteredList[0] = filteredList[1] = False
    c = 0
    for i in range(len(filteredList)):
        if filteredList[i]:
            c += 1
        filteredList[i] = c
    player1 = 0
    for n in nums:
        player1 += filteredList[n] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
