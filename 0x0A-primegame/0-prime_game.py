#!/usr/bin/python3
"""Module defining isWinner function for determining the winner."""


def isWinner(x, nums):
    """Determine who wins most rounds in the prime game.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers for each round's n.

    Returns:
        str: Winner's name ("Maria" or "Ben"), or None if tie.
    """
    if x <= 0 or nums is None or x != len(nums):
        return None

    mariaWinsCount = 0  # Count of Maria's wins
    benWinsCount = 0  # Count of Ben's wins

    for num in nums:
        roundsSet = list(range(1, num + 1))
        primesSet = primes_in_range(1, num)

        if not primesSet:  # Ben wins if no primes
            benWinsCount += 1
            continue

        isMariaTurns = True  # Flag for Maria's turn

        while(True):
            if not primesSet:  # If no primes left, the current player loses
                if isMariaTurns:
                    benWinsCount += 1
                else:
                    mariaWinsCount += 1
                break

            smallestPrime = primesSet.pop(0)
            roundsSet.remove(smallestPrime)

            roundsSet = [x for x in roundsSet if x % smallestPrime != 0]

            isMariaTurns = not isMariaTurns  # Switch turns

    if mariaWinsCount > benWinsCount:
        return "Maria"

    if mariaWinsCount < benWinsCount:
        return "Ben"

    return None  # Return None if there is a tie


def is_prime(n):
    """Return True if n is prime, else False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_in_range(start, end):
    """Return list of primes in the range [start, end]."""
    return [n for n in range(start, end + 1) if is_prime(n)]
