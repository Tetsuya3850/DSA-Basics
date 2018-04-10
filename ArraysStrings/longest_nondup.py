# Given a string, find the length of the longest substring without repeating characters.

def longest_nondup(s):
    i, j = 0, 0
    max_length = 0
    chr_set = set()
    while i < len(s) and j < len(s):
        if s[j] not in chr_set:
            chr_set.add(s[j])
            j += 1
            max_length = max(max_length, j - i)
        else:
            chr_set.remove(s[i])
            i += 1
    return max_length

print (longest_nondup('pwwkew'))
