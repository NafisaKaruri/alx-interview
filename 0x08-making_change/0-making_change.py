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

    dp = [float('inf')] * (total + 1)

    dp[0] = 0

    # Iterate through each coin denomination
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    if dp[total] == float('inf'):
        return -1

    return dp[total]
