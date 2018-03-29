class Node:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    def appendleft(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def pop(self):
        temp = self.head
        if not temp:
            return False
        while temp.next.next:
            temp = temp.next
        data = temp.next.data
        temp.next = None
        return data

    def popleft(self):
        temp = self.head
        if not temp:
            return False
        self.head = temp.next

    def size(self):
        temp = self.head
        count = 0
        if not temp:
            return count
        while temp:
            count += 1
            temp = temp.next
        return count

    def search(self, key):
        temp = self.head
        while temp and temp.data != key:
            temp = temp.next
        if not temp:
            return False
        return True

    def delete(self, key):
        temp = self.head
        if not temp:
            return False
        if temp.data == key:
            self.head = temp.next
            return
        while temp.next:
            if temp.next.data == key:
                temp.next = temp.next.next
                return
            temp = temp.next
        return False

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def printall(self):
        temp = self.head
        while temp:
            print (temp.data, end=" ")
            temp = temp.next
        print()
