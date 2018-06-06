
# Function to find greatest common divisor and least common multiple.


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


print(gcd(12, 18))
print(lcm(12, 18))
