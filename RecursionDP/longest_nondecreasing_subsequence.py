def longest_nondecreasing_subsequence(A):
    # Write a program that takes as input an array of numbers and returns a longest nondecreasing subsequence in the array.
    # Time O(N^2), Space O(N^2), where N is the length of the array.
    longest_nondecreasing_subsequence = [[i] for i in A]
    for i in range(1, len(A)):
        for j in range(i):
            if A[i] >= A[j] and 1 + len(longest_nondecreasing_subsequence[j]) > len(longest_nondecreasing_subsequence[i]):
                longest_nondecreasing_subsequence[i] = longest_nondecreasing_subsequence[j] + [
                    A[i]]

    return max(longest_nondecreasing_subsequence, key=len)


A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
print(longest_nondecreasing_subsequence(A))
