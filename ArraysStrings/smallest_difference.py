# Given two sorted array of integers, compute the pair of values with the samallest difference.

def smallest_difference(A1, A2):
    i, j = 0, 0
    shortest = float('inf')
    while i < len(A1) and j < len(A2):
        shortest = min(shortest, abs(A1[i] - A2[j]))
        if A1[i] <= A2[j]:
            i += 1
        else:
            j += 1
    return shortest

print (smallest_difference([0, 4, 8, 13], [2, 9]))
