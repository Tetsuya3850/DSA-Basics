
def remove_duplicates_sorted_llist(L):
    # Time O(N). Space O(1), where N is the length of the linkedlist.
    it = L
    while it:
        next_distinct = it.next
        while next_distinct and next_distinct.data == it.data:
            next_distinct = next_distinct.next
        it.next = next_distinct
        it = next_distinct
    return L
