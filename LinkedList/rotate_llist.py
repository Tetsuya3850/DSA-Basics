
def cyclically_right_shift_list(L, k):
    # Time O(N), Space O(1), where N is the length of the linkedlist.
    if not L:
        return L
    tail = L
    n = 1
    while tail.next:
        n += 1
        tail = tail.next
    k %= n
    if k == 0:
        return L
    tail.next = L
    steps_to_new_head = n - k
    new_tail = tail
    while steps_to_new_head:
        steps_to_new_head -= 1
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    return new_head
