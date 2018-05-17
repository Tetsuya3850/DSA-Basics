def group_anagrams(A):
    # Time O(NlogN + klogK), Space O(1), where N is the length of the array and k is the maximum length of each string.
    return sorted(A, key=lambda word: ''.join(sorted(word)))


words = ["debitcard", "elvis", "silent", "badcredit",
         "lives", "freedom", "listen", "levis", "money"]
print(group_anagrams(words))
