#!/usr/bin/python3
"""
0-minoperations.py: Contains the minOperations function that calculates
the minimum number of operations needed to achieve exactly n H characters
in a text file using only "Copy All" and "Paste" operations.
"""


def minOperations(n):
    """
    Calculates the minimum number of operations to achieve n H characters

    The function uses prime factorization to determine the number of operations
 required. Each prime factor corresponds to a "Copy All" or "Paste" operation.

    Parameters:
    n (int): The target number of characters.

    Returns:
    int: The min number of operations required to reach exactly n H characters.
    If n is less than or equal to 1, returns 0 as it is impossible to achieve.
    """
    # If impossible to achieve return 0
    if n <= 1:
        return 0

    # operations counter, factors checking starts from 2
    operations = 0
    divisor = 2

    while n > 1:
        # Check if divisor is a factor of n
        while n % divisor == 0:
            operations += divisor
            n //= divisor  # Reduce n by the factor
        divisor += 1  # Move to next factor

    return operations
