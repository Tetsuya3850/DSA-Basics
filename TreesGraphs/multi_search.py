
def multi_search(b, T):
    # O(kt + bk), where k is the length of the longest string in T and b is the length of the b and t is the length of array T.
    t = Trie()
    for s in T:
        t.insert(s)
    result = []
    for i in range(len(b)):
        result.extend(t.all_prefix_search(b[i:]))
    return result


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
        # Time O(N), Space O(1), where N is the length of the key.
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
        # Time O(N), Space O(1), where N is the length of the key.
        curr = self.root
        for level in range(len(key)):
            index = self.char_to_index(key[level])
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return curr != None and curr.end

    def shallow_search(self, key):
        # Time O(N), Space O(1), where N is the length of the key.
        curr = self.root
        for level in range(len(key)):
            index = self.char_to_index(key[level])
            if not curr.children[index]:
                return 0
            curr = curr.children[index]
        return curr.prefix

    def all_prefix_search(self, key):
        # Time O(N), Space O(1), where N is the length of the key.
        valid_prefix = []
        curr = self.root
        for level in range(len(key)):
            index = self.char_to_index(key[level])
            if not curr.children[index]:
                return valid_prefix
            curr = curr.children[index]
            if curr.end:
                valid_prefix.append(key[:level+1])
        return valid_prefix


print(multi_search('mississippi', [
      'is', 'ppi', 'hi', 'sis', 'i', 'ssippi', 'mississippi']))
