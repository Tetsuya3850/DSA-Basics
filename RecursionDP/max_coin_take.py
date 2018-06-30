
def max_coin_take(coins):
    def max_coin_range(a, b):
        if a > b:
            return 0
        if max_coin_table[a][b] == 0:
            max_coin_a = coins[a] + \
                min(max_coin_range(a+2, b), max_coin_range(a+1, b-1))
            max_coin_b = coins[b] + \
                min(max_coin_range(a+1, b-1), max_coin_range(a, b-2))
            max_coin_table[a][b] = max(max_coin_a, max_coin_b)
        return max_coin_table[a][b]

    max_coin_table = [[0] * len(coins) for _ in coins]
    return max_coin_range(0, len(coins)-1)


print(max_coin_take([25, 5, 10, 5, 10, 5, 10, 25, 1, 25, 1, 25, 1, 25, 5, 10]))
