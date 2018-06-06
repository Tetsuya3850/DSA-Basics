class DoubleNode:
    def __init__(self, data=0, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def appendleft(self, new_data):
        # Time O(1), Space O(1), where N is the length of the linkedlist.
        new_node = DoubleNode(new_data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append(self, new_data):
        # Time O(1), Space O(1), where N is the length of the linkedlist.
        new_node = DoubleNode(new_data)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        # Time O(1), Space O(1), where N is the length of the linkedlist.
        temp = self.tail
        if not temp:
            return
        data = temp.data
        self.tail = temp.prev
        if not self.tail:
            self.head = None
        else:
            self.tail.next = None
        return data

    def popleft(self):
        # Time O(1), Space O(1), where N is the length of the linkedlist.
        temp = self.head
        if not temp:
            return
        data = temp.data
        self.head = temp.next
        if not self.head:
            self.tail = None
        else:
            self.head.prev = None
        return data

    def printall(self):
        # Time O(N), Space O(1), where N is the length of the linkedlist.
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


deque = Deque()
deque.append(4)
deque.append(3)
deque.appendleft(2)
deque.pop()
deque.pop()
deque.popleft()
deque.appendleft(2)
deque.printall()
