# Design an algorithm to find all paris of integers within an array which sum to a specified value

from collections import defaultdict

def pair_sum(A, goal_sum):
    complementary_dict = defaultdict(int)
    for num in A:
        complementary = goal_sum - num
        if num in complementary_dict and complementary_dict[num] > 0:
            print (num, complementary)
            complementary_dict[complementary] -= 1
        complementary_dict[complementary] += 1

pair_sum([1, 7, 8, 3, 5, 6, 2, 3], 10)

def pair_sum_sort(A, goal_sum):
    A.sort()
    first, last = 0, len(A) - 1
    while first < last:
        s = A[first] + A[last]
        if s == goal_sum:
            print (A[first], A[last])
            first += 1
            last -= 1
        else:
            if s < goal_sum:
                first += 1
            else:
                last -= 1

pair_sum_sort([1, 7, 8, 3, 5, 6, 2, 3], 10)
