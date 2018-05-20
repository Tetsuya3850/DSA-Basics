from collections import defaultdict


def re_space(s, dictionary):
    # Given a dictionary and the document, design an algorithm to unconcatenate the document in a way that minimizes the number of unrecognized characters.
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
