def find_duplicates(A):
    # You have an array with all the numbers from 1 to N, where N is at most 32000. The array may have duplicate entries and you do not know what N is. With only 4 KB of memory available, how would you print all duplicate elements in the array?
    bit_vector = [0] * 4096
    for num in A:
        if bit_vector[num / 8] & 1 << num % 8:
            print(num)
        else:
            bit_vector[num / 8] |= 1 << num % 8


A = [i for i in range(1, 32001)]
A[0] = 32000
A[1] = 31999
find_duplicates(A)
