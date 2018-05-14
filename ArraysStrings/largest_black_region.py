from collections import deque


def largest_black_region(A):
    # Design an algorithm for computing the black region that contains the most points.
    # Time O(N), Space O(N), where N is the num of grids in matrix.
    def bfs(r, c, visited):
        region = 0
        q = deque()
        q.append((r, c))
        region += 1
        visited.add((r, c))
        while q:
            r, c = q.popleft()
            for d in (0, 1), (0, -1), (1, 0), (-1, 0):
                next_r, next_c = r + d[0], c + d[1]
                if 0 <= next_r < len(A) and 0 <= next_c < len(A[next_r]) and A[next_r][next_c] and (next_r, next_c) not in visited:
                    q.append((next_r, next_c))
                    region += 1
                    visited.add((next_r, next_c))
        return region

    visited = set()
    max_region = 0
    r, c = 0, 0
    while r < len(A) and c < len(A[0]):
        if A[r][c] and (r, c) not in visited:
            region = bfs(r, c, visited)
            max_region = max(max_region, region)
        if r < len(A) - 1:
            r += 1
        else:
            r = 0
            c += 1
    return max_region


A = [[1, 0, 1, 1], [0, 1, 0, 1], [1, 0, 0, 0], [1, 1, 1, 1]]
print(largest_black_region(A))
