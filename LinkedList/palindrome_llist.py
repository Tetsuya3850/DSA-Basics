# Check whether linked list is palindrome.


def palindrome_llist(llist):
    # Time O(N), Space O(N), where N is the length of the linkedlist.
    def is_palindrome_recurse(head, leng):
        if head == None and leng <= 0:
            return Result(head, True)
        elif leng == 1:
            return Result(head.next, True)
        res = is_palindrome_recurse(head.next, leng - 2)
        if not res.result or res.node == None:
            return res
        res.result = (head.data == res.node.data)
        res.node = res.node.next
        return res

    return is_palindrome_recurse(llist.head, llist.size()).result


class Result:
    def __init__(self, node, result):
        self.node = node
        self.result = result


def palindrome_llist_iterative(llist):
    # Time O(N), Space O(N), where N is the length of the linkedlist.
    fast = llist.head
    slow = llist.head
    stack = []
    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next
    if fast:
        slow = slow.next
    while slow:
        top = stack.pop()
        if top != slow.data:
            return False
        slow = slow.next
    return True


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


llist = LinkedList()
llist.appendleft(4)
llist.appendleft(3)
llist.appendleft(3)
llist.appendleft(3)
llist.appendleft(4)
print(palindrome_llist(llist))
print(palindrome_llist_iterative(llist))
