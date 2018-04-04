import math

def sieve_of_eratosthenes(n):
    prime_table = [True] * (n+1)
    prime_table[0] = False
    prime_table[1] = False
    m = math.floor(math.sqrt(n))
    for i in range(2, n+1):
        if prime_table[i]:
            print (i)
            for j in range(i*i, n+1, i):
                prime_table[j] = False

sieve_of_eratosthenes(30)
