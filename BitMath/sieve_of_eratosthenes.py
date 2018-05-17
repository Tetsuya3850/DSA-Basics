import math


def sieve_of_eratosthenes(n):
    # Time O(n), Space O(n), where n is the given num.
    prime_table = [True] * (n+1)
    prime_table[0] = False
    prime_table[1] = False
    m = math.floor(math.sqrt(n))
    for i in range(2, m+1):
        if prime_table[i]:
            for j in range(i*i, n+1, i):
                prime_table[j] = False
    for i in range(2, n+1):
        if prime_table[i]:
            print(i)


sieve_of_eratosthenes(30)
