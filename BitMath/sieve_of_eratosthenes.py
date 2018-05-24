def sieve_of_eratosthenes(n):
    # Time O(n), Space O(n), where n is the given num.
    primes = []
    prime_table = [False, False] + [True] * (n-1)
    for p in range(2, n):
        if prime_table[p]:
            primes.append(p)
            for i in range(p, n+1, p):
                prime_table[i] = False
    return primes


print(sieve_of_eratosthenes(30))
