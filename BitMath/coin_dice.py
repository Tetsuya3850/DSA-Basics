
import random
from collections import Counter


def coin():
    return random.randint(0, 1)


def dice():
    # Make a dice with a coin.
    while True:
        num = 4 * coin() + 2 * coin() + 1 * coin()
        if num < 6:
            return num+1


c = Counter()
for i in range(1000):
    c[dice()] += 1
print(c)
