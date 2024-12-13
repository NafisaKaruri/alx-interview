#!/usr/bin/python3


def sieve_of_eratosthenes(limit):
    """
    Generates a list of primes up to 'limit' using the Sieve of Eratosthenes.
    """
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for i in range(start * start, limit + 1, start):
                sieve[i] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]


def isWinner(x, nums):
    """
    Determines the winner.
    Maria always goes first, and both players play optimally.
    """
    if x <= 0 or nums is None or x != len(nums):
        return None

    ben_wins = 0
    maria_wins = 0

    # Precompute primes up to the maximum possible n in nums using the sieve
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    for n in nums:
        # Generate a list of available numbers (1 to n)
        # and a list to mark removed numbers
        available = [True] * (n + 1)
        available[0] = available[1] = False  # 0 and 1 are not prime

        turn = 0  # 0 for Maria, 1 for Ben
        moves_left = 0  # Counter for available primes

        # Count the primes <= n
        for prime in primes:
            if prime <= n:
                moves_left += 1
            else:
                break

        # Simulate the game
        while moves_left > 0:
            # Find the next available prime number
            for i in range(2, n + 1):
                if available[i]:
                    prime = i
                    break

            # Remove multiples of the chosen prime
            for j in range(prime, n + 1, prime):
                available[j] = False

            # Toggle the turn (Maria -> Ben or Ben -> Maria)
            turn = 1 - turn
            moves_left -= 1

        # If turn is 0, it means Ben made the last valid move, so Maria loses.
        if turn == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if ben_wins > maria_wins:
        return "Ben"
    if maria_wins > ben_wins:
        return "Maria"
    return None
