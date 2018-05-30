def smallest_k(A, k):
    def smallest_k_helper(A, k, result):
        partition = A[0]
        smaller, larger = [], []
        for i in range(1, len(A)):
            if A[i] < partition:
                smaller.append(A[i])
            else:
                larger.append(A[i])
        partition_order = len(smaller) + 1
        if partition_order == k:
            return result + smaller + [partition]
        elif partition_order > k:
            return smallest_k_helper(smaller, k, result)
        else:
            return smallest_k_helper(larger, k-partition_order, result + smaller + [partition])
    return smallest_k_helper(A, k, [])


print(smallest_k([1, 9, 4, 3, 7, 10, 5, 2], 6))


# An algorithm for finding the median of an array.

import operator
import random


def find_kth_largest(k, A):
    # Time O(N), Space O(1), where N is the length of the array.
    def partition_around_pivot(left, right, pivot_idx):
        pivot_value = A[pivot_idx]
        new_pivot_idx = left
        A[pivot_idx], A[right] = A[right], A[pivot_idx]
        for i in range(left, right):
            if operator.gt(A[i], pivot_value):
                A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
                new_pivot_idx += 1
        A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]
        return new_pivot_idx

    left, right = 0, len(A) - 1
    while left <= right:
        pivot_idx = random.randint(left, right)
        new_pivot_idx = partition_around_pivot(left, right, pivot_idx)
        if new_pivot_idx == k - 1:
            return A[new_pivot_idx]
        elif new_pivot_idx > k - 1:
            right = new_pivot_idx - 1
        else:
            left = new_pivot_idx + 1


class BinaryTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left, self.right = None, None
        self.size = 1

    def insert(self, d):
        if d <= self.data:
            if not self.left:
                self.left = BinaryTreeNode(d)
            else:
                self.left.insert(d)
        else:
            if not self.right:
                self.right = BinaryTreeNode(d)
            else:
                self.right.insert(d)
        self.size += 1

    def get_ith_node(self, i):
        left_size = self.left.size if self.left else 0
        if i < left_size:
            return self.left.get_ith_node(i)
        elif i == left_size:
            return self.data
        else:
            return self.right.get_ith_node(i - (left_size + 1))

    def get_node_rank(self, k):
        if k == self.data:
            return self.left.size if self.left else 0
        elif k < self.data:
            return self.left.get_node_rank(k)
        else:
            return (self.left.size if self.left else 0) + 1 + self.right.get_node_rank(k)


root = BinaryTreeNode(20)
root.insert(5)
root.insert(1)
root.insert(4)
root.insert(4)
root.insert(5)
root.insert(9)
root.insert(7)
root.insert(13)
root.insert(3)
print(root.get_node_rank(1))
print(root.get_node_rank(3))
print(root.get_node_rank(4))
print(root.get_ith_node(0))
