
def longest_nondup(s):
    # Given a string, find the length of the longest substring without repeating characters.
    # Time O(N), Space O(M), where N is the length of string and M is the num of unique chars in string.
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


print(longest_nondup('pwwkew'))
