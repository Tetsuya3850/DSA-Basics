
def sum_llists_reverse(llist1, llist2):
    # Time complexity O(A+B). Space complexity O(A+B).
    len1 = llist1.size()
    len2 = llist2.size()
    if len1 < len2:
        llist1 = padList(llist1, len2 - len1)
    else:
        llist2 = padList(llist2, len1 - len2)
    sum = addListsHelper(llist1.head, llist2.head)
    if sum.carry:
        sum.sum.appendleft(sum.carry)
    return sum.sum


def padList(llist, pad):
    for _ in range(pad):
        llist.appendleft(0)
    return llist


def addListsHelper(llist1, llist2):
    if not llist1 and not llist2:
        sum = Partial_Sum()
        return sum
    sum = addListsHelper(llist1.next, llist2.next)
    val = sum.carry + llist1.data + llist2.data
    sum.sum.appendleft(val % 10)
    sum.carry = val // 10
    return sum


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

    def printall(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


class Partial_Sum:
    sum = LinkedList()
    carry = 0


llist1 = LinkedList()
llist1.appendleft(6)
llist1.appendleft(1)
llist1.appendleft(7)
llist2 = LinkedList()
llist2.appendleft(3)
llist2.appendleft(9)
llist2.appendleft(5)
sum_llists_reverse(llist1, llist2).printall()
