
def loop_llist(llist):
    # Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.
    # Time O(N), Space O(1), where N is the length of the linkedlist.
    fast = llist.head
    slow = llist.head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    if not fast or not fast.next:
        return False
    new_pointer = llist.head
    while new_pointer != slow:
        new_pointer = new_pointer.next
        slow = slow.next
    return slow


class Node:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None


llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
forth = Node(4)
llist.head.next = second
second.next = third
third.next = forth
forth.next = second
print(loop_llist(llist))
