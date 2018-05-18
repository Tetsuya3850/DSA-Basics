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
