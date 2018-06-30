from collections import defaultdict
import random


class RandomizedSet:
    def __init__(self):
        self.elements = []
        self.index_lookup = defaultdict()

    def insert(self, val):
        if val not in self.index_lookup:
            self.elements.append(val)
            self.index_lookup[val] = len(self.elements) - 1
            return True
        return False

    def remove(self, val):
        if val in self.index_lookup:
            index = self.index_lookup[val]
            self.elements[index], self.elements[-1] = self.elements[-1], self.elements[index]
            self.index_lookup[self.elements[index]] = index
            del self.index_lookup[val]
            self.elements.pop()
            return True
        return False

    def getRandom(self):
        return self.elements[random.randrange(len(self.elements))]
