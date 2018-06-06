
from collections import deque


def largest_black_region(matrix):
    # Design an algorithm for computing the black region that contains the most points.
    # Time O(WH) where W is the width and H is the height of matrix.
    visited = set()
    max_region = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] and (r, c) not in visited:
                curr_region = dfs(r, c, matrix, visited)
                max_region = max(max_region, curr_region)
    return max_region


def bfs(r, c, matrix, visited):
    curr_region = 0
    q = deque()
    q.append((r, c))
    curr_region += 1
    visited.add((r, c))
    while q:
        r, c = q.popleft()
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_r, next_c = r + d[0], c + d[1]
            if isValid(next_r, next_c, matrix, visited):
                q.append((next_r, next_c))
                curr_region += 1
                visited.add((next_r, next_c))
    return curr_region


def dfs(r, c, matrix, visited):
    def helper(r, c, matrix, visited):
        curr_region = 1
        visited.add((r, c))
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_r, next_c = r + d[0], c + d[1]
            if isValid(next_r, next_c, matrix, visited):
                curr_region += helper(next_r, next_c, matrix, visited)
        return curr_region

    return helper(r, c, matrix, visited)


def isValid(r, c, matrix, visited):
    return 0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and matrix[r][c] and (r, c) not in visited


A = [[1, 0, 1, 1], [0, 1, 0, 1], [1, 0, 0, 0], [1, 1, 1, 1]]
print(largest_black_region(A))
