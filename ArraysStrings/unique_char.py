# Determine if a string has all unique characters. You may assume the string to be all lowercase abc.

def unique_char(s):
    checker = 0
    for ch in s:
        val = ord(ch) - 97
        if (checker & (1 << val)) > 0:
            return False
        checker |= (1 << val)
    return True

s = 'kaisei'
print (unique_char(s))
