
def counting_sort(A):
    # Time O(N+k), Space O(N+k), where N is the length of the array and k is the range of nums.
    count_table = [0] * 10
    output = [0] * len(A)
    for num in A:
        count_table[num] += 1
    for i in range(1, 10):
        count_table[i] = count_table[i] + count_table[i-1]
    for num in A:
        idx = count_table[num] - 1
        output[idx] = num
        count_table[num] -= 1
    return output


A = [1, 4, 1, 2, 7, 5, 2]
print(counting_sort(A))
