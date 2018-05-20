
from collections import deque


def weave_lists(A1, A2):
    # Merge two arrays in all possible ways, while keeping the same relative order.
    def weave_lists_helper(d1, d2, prefix):
        if not d1 or not d2:
            nonlocal results
            result = prefix[:]
            result.extend(d1)
            result.extend(d2)
            results.append(result)
            return

        head_first = d1.popleft()
        prefix.append(head_first)
        weave_lists_helper(d1, d2, prefix)
        prefix.pop()
        d1.appendleft(head_first)

        head_second = d2.popleft()
        prefix.append(head_second)
        weave_lists_helper(d1, d2, prefix)
        prefix.pop()
        d2.appendleft(head_second)

    results = []
    deque_A1 = deque(A1)
    deque_A2 = deque(A2)
    weave_lists_helper(deque_A1, deque_A2, [])
    return results


print(weave_lists([1, 2], [3, 4]))
