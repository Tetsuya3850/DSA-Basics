from collections import defaultdict


def group_anagrams(dictionary):
    # A program that takes as input a set of words and returns groups of anagrams for those words.
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
