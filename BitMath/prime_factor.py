# Program to print all prime factors of a given number.

import math

def prime_factor(n):
    result = []

    while n % 2 == 0:
        result.append(2)
        n //= 2

    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            result.append(i)
            n //= i

    if n > 2:
        result.append(n)

    return result

print prime_factor(315)
