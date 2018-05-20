
def num_ways(n, m, obstacles):
    # Write a program that counts how many ways you can go from the top-left to the bottom-right in a 2D array, in the presence of obstacles.
    def helper(x, y):
        if x == y == 0:
            return 1

        if num_ways[x][y] == 0:
            ways_top = 0 if x == 0 or obstacles[x -
                                                1][y] else helper(x - 1, y)
            ways_left = 0 if y == 0 or obstacles[x][y -
                                                    1] else helper(x, y - 1)
            num_ways[x][y] = ways_top + ways_left
        return num_ways[x][y]

    num_ways = [[0] * m for _ in range(n)]
    return helper(n - 1, m - 1)


n = 4
m = 4
obstacles = [[False, False, False, False], [False, True, False, False], [
    False, False, False, False], [False, False, False, False]]
print(num_ways(n, m, obstacles))
