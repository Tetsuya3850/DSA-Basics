

def group_anagrams(A):
    return sorted(A, key=lambda word: ''.join(sorted(word)))

dictionary = ["debitcard", "elvis", "silent", "badcredit", "lives", "freedom", "listen", "levis", "money"]
print (group_anagrams(dictionary))
