from collections import defaultdict


def re_space(s, dictionary):
    # Time O(N^2), Space O(N), where N is the length of string.
    def helper(s, dictionary, start, cache):
        if start >= len(s):
            return (0, "")
        if start not in cache:
            bestInvalid = float('inf')
            bestParsing = ""
            partial = ""
            index = start
            while index < len(s):
                c = s[index]
                partial += c
                invalid = 0 if partial in dictionary else len(partial)
                if invalid < bestInvalid:
                    result = helper(s, dictionary, index+1, cache)
                    if invalid + result[0] < bestInvalid:
                        bestInvalid = invalid + result[0]
                        bestParsing = partial + " " + result[1]
                        if bestInvalid == 0:
                            break
                index += 1
            cache[start] = (bestInvalid, bestParsing)
        return cache[start]

    cache = defaultdict()
    helper(s, dictionary, 0, cache)
    return cache[0][1]


s = "jesslookedjustliketimherbrother"
dictionary = ["looked", "look", "just", "like",
              "her", "brother", "us", "herb", "other", "i", "a"]
print(re_space(s, dictionary))


def decompose_dict_words(s, dictionary):
    last_length = [-1] * len(s)
    for i in range(len(s)):
        if s[:i+1] in dictionary:
            last_length[i] = i+1
        if last_length[i] == -1:
            for j in range(i):
                if last_length[j] != -1 and s[j+1: i+1] in dictionary:
                    last_length[i] = i - j
                    break
    decompositions = []
    if last_length[-1] != -1:
        idx = len(s) - 1
        while idx >= 0:
            decompositions.append(s[idx + 1 - last_length[idx]: idx + 1])
            idx -= last_length[idx]
        decompositions = decompositions[::-1]
    return decompositions


s = "aman"
dictionary = ["am", "an", "a"]
print(decompose_dict_words(s, dictionary))
