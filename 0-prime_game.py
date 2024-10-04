#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """ Returns a list of boolean values where True indicates prime numbers up to n """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes

def count_primes_up_to(n, sieve):
    """ Count how many primes are less than or equal to n """
    return sum(sieve[:n+1])

def isWinner(x, nums):
    """ Determines who the winner is after x rounds """
    if not nums or x < 1:
        return None
    
    # Find primes up to the maximum number in nums
    max_num = max(nums)
    sieve = sieve_of_eratosthenes(max_num)

    # Maria and Ben's win counters
    maria_wins = 0
    ben_wins = 0

    # Simulate each round
    for n in nums:
        # Count how many primes are up to and including n
        primes_count = count_primes_up_to(n, sieve)

        # Maria wins if the count of primes is odd, Ben wins if it's even
        if primes_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage
if __name__ == "__main__":
    print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))

