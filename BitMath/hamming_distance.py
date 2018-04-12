
def hamming_distance(a, b):
    diff = a ^ b
    count = 0
    while diff:
        diff &= (diff - 1)
        count += 1
    return count

print (hamming_distance(17, 5))
