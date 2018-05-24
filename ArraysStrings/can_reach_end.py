
def can_reach_end(A):
    # Time O(N), Space O(1), where N is the length of the array.
    furthest_so_far = 0
    last_i = len(A) - 1
    i = 0
    while i <= furthest_so_far and furthest_so_far < last_i:
        furthest_so_far = max(furthest_so_far, A[i] + i)
        i += 1
    return furthest_so_far >= last_i


print(can_reach_end([3, 2, 0, 0, 2, 0, 1]))
print(can_reach_end([3, 3, 1, 0, 2, 0, 1]))
