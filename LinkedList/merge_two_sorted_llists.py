
class ListNode():
    def __init__(self):
        self.val = None
        self.next = None


def merge_two_sorted_llists(L1, L2):
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next
        tail = tail.next

    tail.next = L1 or L2
    return dummy_head.next
