# Given two strings, write a method to decide if one is a permutation of the other.

from collections import Counter


def strings_permutation_sort(s1, s2):
    # Time O(AlogA + BlogB), Space O(1), where A is the length of s1 and B is the length of s2.
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


def strings_permutation_table(s1, s2):
    # Time O(A + B), Space O(1), where A is the length of s1 and B is the length of s2.
    if len(s1) != len(s2):
        return False
    char_table = [0] * 128
    for char in s1:
        char_table[ord(char)] += 1
    for char in s2:
        if char_table[ord(char)] == 0:
            return False
        char_table[ord(char)] -= 1
    return True


def strings_permutation_counter(s1, s2):
    # Time O(A + B), Space O(A + B), where A is the length of s1 and B is the length of s2.
    return Counter(s1) == Counter(s2)


s1 = 'cracking'
s2 = 'rkicgacn'
print(strings_permutation_sort(s1, s2))
print(strings_permutation_table(s1, s2))
print(strings_permutation_counter(s1, s2))
