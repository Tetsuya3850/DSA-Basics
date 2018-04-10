# Write a function that adds two numbers. You should not use any arithmetic operators
def add(a, b):
    running_sum, carryin, k, temp_a, temp_b = 0, 0, 1, a, b
    while temp_a or temp_b:
        ak, bk = a & k, b & k
        carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
        running_sum |= ak ^ bk ^ carryin
        carryin, k, temp_a, temp_b = (carryout << 1, k << 1, temp_a >> 1, temp_b >> 1)
    return running_sum | carryin

print add(3, 9)
