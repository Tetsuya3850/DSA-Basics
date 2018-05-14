class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self):
        self.table = [None] * 101

    def hash(self, key):
        # Generate hash from key.
        # Time O(N), Space O(1), where N is the length of key.
        hashed = 0
        for i in range(len(key)):
            hashed = (256 * hashed + ord(key[i])) % 101
        return hashed

    def add(self, key, value):
        # Add key, value.
        # Time O(1), Space O(1), where N is the num of elements in hashtable.
        bucket = self.hash(key)
        if not self.table[bucket]:
            self.table[bucket] = HashNode(key, value)
        else:
            self.table[bucket].next = HashNode(key, value)

    def find(self, key):
        # Find value from key.
        # Time O(1), Space O(1), where N is the num of elements in hashtable.
        bucket = self.hash(key)
        if not self.table[bucket]:
            return False
        else:
            temp = self.table[bucket]
            while temp:
                if temp.key == key:
                    return temp.value
                temp = temp.next
            return False

    def delete(self, key):
        # Delete key, value.
        # Time O(1), Space O(1), where N is the num of elements in hashtable.
        bucket = self.hash(key)
        if not self.table[bucket]:
            return False
        else:
            if self.table[bucket].key == key:
                self.table[bucket] = None
            else:
                temp = self.table[bucket]
                while temp:
                    if temp.next.key == key:
                        temp.next = temp.next.next
                        return
                    temp = temp.next
                return False


my_hash = HashTable()
my_hash.add('apple', '2$')
my_hash.add('banana', '3$')
print(my_hash.find('apple'))
print(my_hash.find('orange'))
my_hash.delete('banana')
print(my_hash.find('banana'))
