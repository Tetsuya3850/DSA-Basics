
from collections import deque
INT_MAX = 4294967296


def kth_multiple_357(k):
    # Design an algorithm to find the kth number such that the only prime factors are 3, 5, 7.
    # Time O(k), where k is the specified order.
    if k < 0:
        return 0
    val = 0
    three_queue = deque()
    five_queue = deque()
    seven_queue = deque()
    three_queue.append(1)
    for _ in range(k):
        v3 = three_queue[0] if len(three_queue) > 0 else INT_MAX
        v5 = five_queue[0] if len(five_queue) > 0 else INT_MAX
        v7 = seven_queue[0] if len(seven_queue) > 0 else INT_MAX
        val = min(v3, v5, v7)
        if val == v3:
            three_queue.popleft()
            three_queue.append(val * 3)
            five_queue.append(val * 5)
        elif val == v5:
            five_queue.popleft()
            five_queue.append(val * 5)
        else:
            seven_queue.popleft()
        seven_queue.append(val * 7)
    return val


print(kth_multiple_357(1))
