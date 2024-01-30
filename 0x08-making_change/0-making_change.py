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
    few_number = int(total / coins[0])
    fn = few_number
    remain = total - few_number * coins[0]
    idx = 0

    for i in range(1, len(coins)):
        few_number = int(remain / coins[i])
        idx = i
        if few_number == 0:
            pass
        remain = remain - few_number * coins[i]
        fn = fn + few_number
        if remain == 0:
            return fn

    if remain in coins:
        return fn + 1
    return -1
