
def find_duplicates(A):
    # Only 4 KB of memory available.
    class BitSet:
        def __init__(self, size):
            self.bitset = [0] * ((size >> 5) + 1)

        def get(self, pos):
            section_num = pos >> 5
            bit_num = pos & 0x1F
            return (self.bitset[section_num] & (1 << bit_num)) != 0

        def set(self, pos):
            section_num = pos >> 5
            bit_num = pos & 0x1F
            self.bitset[section_num] |= 1 << bit_num

    bit_vector = BitSet(32000)
    for num in A:
        if bit_vector.get(num-1):
            print(num)
        else:
            bit_vector.set(num-1)


A = [i for i in range(1, 32001)]
A[0] = 32000
A[1] = 31999
find_duplicates(A)
