#!/usr/bin/python3
"""
Function to determine the fewest number of coins to make a total amount.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins to make up a total amount.

    Args:
        coins (list): A list of coin denominations.
        total (int): The target amount.

    Returns:
        int: The minimum number of coins needed to make up the total.
             Returns -1 if the total cannot be made with the given coins.
    """
    if total <= 0:
        return 0

    if not coins or coins is None:
        return -1

    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
