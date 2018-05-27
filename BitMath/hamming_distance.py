
def hamming_distance(a, b):
    # Time O(k), where k is the num of 1s in a XOR b.
    diff = a ^ b
    count = 0
    while diff:
        diff &= (diff - 1)
        count += 1
    return count


print(hamming_distance(17, 5))


def total_hamming_dist(nums):
    # Time O(N), Space O(1), where N is the length of [int].
    count_table = [[0, 0] for _ in range(32)]
    for num in nums:
        str_bits = '{:032b}'.format(num)
        for i in range(len(str_bits)):
            if str_bits[i] == '0':
                count_table[i][0] += 1
            else:
                count_table[i][1] += 1
    result = 0
    for counts in count_table:
        result += counts[0] * counts[1]
    return result
