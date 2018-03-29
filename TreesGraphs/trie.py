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
        for level in range(len(key)):
            index = self.char_to_index(key[level])
            if not curr.children[index]:
                return 0
            curr = curr.children[index]
        return curr.prefix

    def delete(self, key):
        def delete_helper(curr_node, key, level, length):
            if curr_node:
                curr_node.prefix -= 1
                if level == length:
                    if curr_node.end:
                        curr_node.end = False
                    return curr_node.has_no_children()
                else:
                    index = self.char_to_index(key[level])
                    if delete_helper(curr_node.children[index], key, level+1, length):
                        curr_node.children[index] = None
                        return not curr_node.end and curr_node.has_no_children()
            return False
        if len(key) == 0:
            return
        delete_helper(self.root, key, 0, len(key))

my_trie = Trie()
my_trie.insert('the')
my_trie.insert('a')
my_trie.insert('there')
my_trie.insert('anaswe')
my_trie.insert('any')
my_trie.insert('by')
my_trie.insert('their')
print (my_trie.search('their'))
print (my_trie.search('an'))
my_trie.delete('their')
print (my_trie.search('their'))
print (my_trie.shallow_search('c'))
print (my_trie.shallow_search('the'))
print (my_trie.shallow_search(''))
print (my_trie.shallow_search('an'))
