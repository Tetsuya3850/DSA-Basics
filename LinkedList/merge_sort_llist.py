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
        while temp:
            print(temp.data)
            temp = temp.next

    def merge_sort(self):
        def get_middle_from_node(head):
            slow = head
            fast = head
            while fast and fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def sorted_merge(l, r):
            result = None
            if not l:
                return r
            if not r:
                return l
            if l.data <= r.data:
                result = l
                result.next = sorted_merge(l.next, r)
            else:
                result = r
                result.next = sorted_merge(l, r.next)
            return result

        def helper(head):
            if not head or not head.next:
                return head
            middle = get_middle_from_node(head)
            next_to_middle = middle.next
            middle.next = None
            left = helper(head)
            right = helper(next_to_middle)
            return sorted_merge(left, right)

        self.head = helper(self.head)


llist = LinkedList()
llist.push(15)
llist.push(10)
llist.push(5)
llist.push(20)
llist.push(3)
llist.push(2)
llist.merge_sort()
llist.printList()
