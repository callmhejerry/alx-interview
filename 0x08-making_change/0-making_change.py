#!/usr/bin/python3

"""
makeChange
"""


def makeChange(coins, total):
    """
    Args:
      - coins (list): list of the values of the coins in possession
      - total (int): given amount
    """
    if total <= 0:
        return 0

    if coins == []:
        return -1

    coins = sorted(coins, reverse=True)
    results = []
    count = 0
    for i in range(len(coins)):
        while coins[i] <= total:
            total = total - coins[i]
            count = count + 1
            results.append(coins[i])

    if total == 0:
        return count
    else:
        return -1
