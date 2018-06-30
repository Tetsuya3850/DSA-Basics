
def unique_char(s):
    # Time O(N), Space O(1), where N is the length of s.
    checker = 0
    for ch in s:
        val = ord(ch) - 97
        if (checker & (1 << val)) > 0:
            return False
        checker |= (1 << val)
    return True


s = 'kaisei'
print(unique_char(s))
