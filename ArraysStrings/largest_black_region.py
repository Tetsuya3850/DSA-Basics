# Design an algorithm for computing the black region that contains the most points.

from collections import deque

def largest_black_region(A):
    visited_points = set()
    max_region = 0
    r, c = 0, 0
    while r < len(A) and c < len(A[0]):
        if A[r][c] and (r, c) not in visited_points:
            current_region = 1
            q = deque()
            q.append((r, c))
            visited_points.add((r, c))
            while q:
                r, c = q.popleft()
                for d in (0, 1), (0, -1), (1, 0), (-1, 0):
                    next_r, next_c = r + d[0], c + d[1]
                    if 0 <= next_r < len(A) and 0 <= next_c < len(A[next_r]) and A[next_r][next_c] and (next_r, next_c) not in visited_points:
                        q.append((next_r, next_c))
                        current_region += 1
                        visited_points.add((next_r, next_c))
            max_region = max(max_region, current_region)
        if r < len(A) - 1:
            r += 1
        else:
            r = 0
            c += 1
    return max_region

A = [[1, 0, 1, 1],[0, 1, 0, 1],[1, 0, 0, 0],[1, 1, 1, 1]]
print (largest_black_region(A))
