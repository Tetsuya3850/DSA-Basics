
class Node:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def partition_llist(self, x):
        # Time complexity O(N). Space complexity O(N).
        it = self.head
        head_low = tail_low = Node()
        head_same = tail_same = Node()
        head_high = tail_high = Node()

        while it:
            if it.data < x:
                tail_low.next = Node(it.data)
                tail_low = tail_low.next
            elif it.data == x:
                tail_same.next = Node(it.data)
                tail_same = tail_same.next
            else:
                tail_high.next = Node(it.data)
                tail_high = tail_high.next
            it = it.next

        tail_low.next = head_same.next
        tail_same.next = head_high.next
        self.head = head_low.next


llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(10)
llist.push(5)
llist.push(8)
llist.push(5)
llist.push(3)
llist.partition_llist(5)
llist.printList()
