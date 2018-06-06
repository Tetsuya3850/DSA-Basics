
from collections import defaultdict


def all_permutations(s):
    # Time complexity O(N^2N!) Space complexity O(N!), where N is the length of ths string.
    def perm_helper(remain_s):
        if not len(remain_s):
            return [""]
        ch = remain_s[0]
        without_ch = perm_helper(remain_s[1:])
        result = []
        for part_result in without_ch:
            for i in range(len(part_result) + 1):
                new_result = part_result[:i] + ch + part_result[i:]
                result.append(new_result)
        return result

    return perm_helper(s)


print(all_permutations('abc'))


def all_permutations_other(s):
    # Time complexity O(NN!), Space complexity O(N), where N is the length of ths string.
    def helper(A, l):
        if l == len(A)-1:
            print("".join(A))
            return
        for i in range(l, len(A)):
            A[l], A[i] = A[i], A[l]
            helper(A, l+1)
            A[l], A[i] = A[i], A[l]
    helper(list(s), 0)


all_permutations_other('abc')


def all_permutations_non_unique(s):
    # Time complexity O(N^2N!), Space complexity O(N), where N is the length of ths string.
    def perm_nonu_helper(part_result, remaining_dict):
        if len(part_result) == len(s):
            print(part_result)
            return

        for item in remaining_dict.keys():
            count = remaining_dict[item]
            if count > 0:
                remaining_dict[item] -= 1
                perm_nonu_helper(part_result + item, remaining_dict)
                remaining_dict[item] += 1

    d = defaultdict(int)
    for ch in s:
        d[ch] += 1
    perm_nonu_helper('', d)


all_permutations_non_unique('aabc')


def all_anagrams(s, trie_dict):
    # Time complexity O(N^2N!), Space complexity O(N), where N is the length of ths string.
    def all_anagrams_helper(partial_result, remaining_s):
        if len(partial_result) == len(s):
            if trie_dict.search(partial_result):
                print(partial_result)
                return
        for i in range(len(remaining_s)):
            if trie_dict.shallow_search(partial_result + remaining_s[i]):
                all_anagrams_helper(
                    partial_result + remaining_s[i], remaining_s[:i] + remaining_s[i+1:])

    all_anagrams_helper("", s)


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False
        self.prefix = 0

    def has_no_children(self):
        for child in self.children:
            if child:
                return False
        return True


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def char_to_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key):
        if len(key) == 0:
            return
        curr = self.root
        curr.prefix += 1
        for level in range(len(key)):
            index = self.char_to_index(key[level])
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
            curr.prefix += 1
        curr.end = True

    def search(self, key):
        curr = self.root
        for level in range(len(key)):
            index = self.char_to_index(key[level])
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return curr != None and curr.end

    def shallow_search(self, key):
        curr = self.root
        length = len(key)
        for level in range(length):
            index = self.char_to_index(key[level])
            if not curr.children[index]:
                return 0
            curr = curr.children[index]
        return curr.prefix


my_trie = Trie()
my_trie.insert("god")
my_trie.insert("dog")
all_anagrams("god", my_trie)
