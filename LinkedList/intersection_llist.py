def intersection_llist(llist1, llist2):
    len1 = llist1.size()
    len2 = llist2.size()
    diff = abs(len1 - len2)
    if len1 < len2:
        llist1, llist2 = llist2, llist1
    head1 = llist1.head
    head2 = llist2.head
    for _ in range(diff):
        head1 = head1.next
    while head1 and head1 != head2:
        head1 = head1.next
        head2 = head2.next
    return head1

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

    def size(self):
        temp = self.head
        count = 0
        if not temp:
            return count
        while temp:
            count += 1
            temp = temp.next
        return count

llist1 = LinkedList()
llist1.head  = Node(1)
second = Node(2)
third  = Node(3)
forth = Node(4)
llist1.head.next = second
second.next = third
third.next = forth

llist2 = LinkedList()
llist2.head = Node(1)
fifth = Node(5)
llist2.head.next = fifth
fifth.next = third

print (intersection_llist(llist1, llist2))
