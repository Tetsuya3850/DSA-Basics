from collections import defaultdict


def pair_sum(A, goal_sum):
    # Design an algorithm to find all paris of integers within an array which sum to a specified value.
    # Elements can only be used once.
    # Time O(N), Space O(N), where N is the length of array.
    complementary_dict = defaultdict(int)
    results = []
    for num in A:
        complementary = goal_sum - num
        if num in complementary_dict and complementary_dict[num] > 0:
            results.append([num, complementary])
            complementary_dict[num] -= 1
        else:
            complementary_dict[complementary] += 1
    return results


print(pair_sum([1, 7, 8, 3, 5, 6, 2, 7, 3], 10))


def pair_sum_sort(A, goal_sum):
    # Time O(NlogN), Space O(1), where N is the length of the array.

    A.sort()
    first, last = 0, len(A) - 1
    results = []
    while first < last:
        s = A[first] + A[last]
        if s == goal_sum:
            results.append([A[first], A[last]])
            first += 1
            last -= 1
        elif s < goal_sum:
            first += 1
        else:
            last -= 1
    return results


print(pair_sum_sort([1, 7, 8, 3, 5, 6, 2, 7, 3], 10))
