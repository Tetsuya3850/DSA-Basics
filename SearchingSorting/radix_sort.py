# Time complexity O(kN) Space complexity O(1)
def radix_sort(A):
    def counting_sort_radix(A, exp):
        count_table = [0] * 10
        output = [0] * len(A)
        for num in A:
            digit = (num // exp) % 10
            count_table[digit] += 1
        for i in range(1, 10):
            count_table[i] = count_table[i] + count_table[i-1]
        i = len(A) - 1
        while i >= 0:
            digit = (A[i] // exp) % 10
            output[count_table[digit] - 1] = A[i]
            count_table[digit] -= 1
            i -= 1
        return output

    max1 = max(A)
    exp = 1
    while max1 // exp > 0:
        A = counting_sort_radix(A, exp)
        exp *= 10
    return A

A = [170, 45, 75, 90, 802, 24, 2, 66]
print (radix_sort(A))
