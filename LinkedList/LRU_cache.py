from collections import defaultdict

class DoubleNode:
    def __init__(self, data=0, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

class Cache:
    def __init__(self):
        self.head = None
        self.tail = None
        self.capacity = 3
        self.size = 0
        self.dict = defaultdict()

    def lookup(self):
        temp = self.tail
        while temp:
            print (temp.data, end=' ')
            temp = temp.prev
        print()

    def update(self, page):
        if page in self.dict:
            self.movetop(page)
        else:
            if self.size < self.capacity:
                self.enqueue(page)
            else:
                self.dequeue()
                self.enqueue(page)

    def enqueue(self, data):
        new_node = DoubleNode(data)
        if not self.size:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        self.dict[data] = new_node

    def dequeue(self):
        if not self.size:
            return
        temp = self.head
        data = temp.data
        self.head = temp.next
        if not self.head:
            self.tail = None
        else:
            self.head.prev = None
        self.size -= 1
        del self.dict[data]
        return data

    def movetop(self, page):
        target = self.dict[page]
        if target == self.tail:
            return
        target_prev = target.prev
        target_next = target.next
        target.prev = self.tail
        target.next = None
        self.tail.next = target
        if target != self.head:
            target_prev.next = target_next
        target_next.prev = target_prev
        if target == self.head:
            self.head = target_next
        self.tail = target

LRU = Cache()
LRU.update(1)
LRU.lookup()
LRU.update(2)
LRU.lookup()
LRU.update(3)
LRU.lookup()
LRU.update(4)
LRU.lookup()
LRU.update(1)
LRU.lookup()
LRU.update(2)
LRU.lookup()
LRU.update(5)
LRU.lookup()
LRU.update(1)
LRU.lookup()
LRU.update(2)
LRU.lookup()
LRU.update(3)
LRU.lookup()
LRU.update(4)
LRU.lookup()
LRU.update(5)
LRU.lookup()
