#!/usr/bin/python3
"""
Prime Game
"""


def findMultiples(num, targets):
    """
    Finds multiples of a given number within a list
    """
    for i in targets:
      def isWinner(x, nums):
    # function to generate list of primes up to n
    def generatePrimes(n):
        sieve = [True] * (n+1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n**0.5)+1):
            if sieve[i]:
                for j in range(i*i, n+1, i):
                    sieve[j] = False
        return [i for i in range(n+1) if sieve[i]]

    # initialize variables to keep track of wins
    maria_wins = 0
    ben_wins = 0

    # simulate the game for each round
    for i in range(x):
        n = nums[i]
        primes = generatePrimes(n)
        maria_moves = 0
        ben_moves = 0
        while primes:
            # Maria's turn
            if maria_moves == ben_moves:
                # find the largest prime that is still in the list
                p = None
                for prime in reversed(primes):
                    if prime is not None:
                        p = prime
                        break
                if p is None:
                    # no primes left, Ben wins
                    ben_wins += 1
                    break
                # remove p and its multiples from the list
                for i in range(p, n+1, p):
                    primes[i-1] = None
                maria_moves += 1
            # Ben's turn
            else:
                # find the largest prime that is still in the list
                p = None
                for prime in reversed(primes):
                    if prime is not None:
                        p = prime
                        break
                if p is None:
                    # no primes left, Maria wins
                    maria_wins += 1
                    break
                # remove p and its multiples from the list
                for i in range(p, n+1, p):
                    primes[i-1] = None
                ben_moves += 1

    # determine the winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
