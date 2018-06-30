
from collections import defaultdict


def group_anagrams(dictionary):
    # Time O(NM), where N is the max length of string and M is the num of strings in dictionary.
    hashed_string_to_anagrams = defaultdict(list)
    for s in dictionary:
        counter = [0] * 26
        for a in s:
            counter[ord(a) - 97] += 1
        stringBuilder = []
        for i, count in enumerate(counter):
            if count > 0:
                stringBuilder.append(str(count))
                stringBuilder.append(chr(i + 97))
        hash = ''.join(stringBuilder)
        hashed_string_to_anagrams[hash].append(s)

    return [group for group in hashed_string_to_anagrams.values()]


dictionary = ["debitcard", "elvis", "silent", "badcredit",
              "lives", "freedom", "listen", "levis", "money"]
print(group_anagrams(dictionary))


def group_anagrams_sort(A):
    # Time O(NlogN + MlogM), where N is the max length of string and M is the num of strings in dictionary.
    return sorted(A, key=lambda word: ''.join(sorted(word)))


words = ["debitcard", "elvis", "silent", "badcredit",
         "lives", "freedom", "listen", "levis", "money"]
print(group_anagrams_sort(words))
