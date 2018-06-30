
from collections import deque


class QueueWithMax:
    def __init__(self):
        self.entries = deque()
        self.cand_max = deque()

    def enqueue(self, x):
        # Time O(1), where N is the num of elements in queue.
        self.entries.append(x)
        while self.cand_max and self.cand_max[-1] < x:
            self.cand_max.pop()
        self.cand_max.append(x)

    def dequeue(self):
         # Time O(1), where N is the num of elements in queue.
        if self.entries:
            result = self.entries.popleft()
            if result == self.cand_max[0]:
                self.cand_max.popleft()
            return result
        raise IndexError('empty queue')

    def max(self):
         # Time O(1), where N is the num of elements in queue.
        if self.cand_max:
            return self.cand_max[0]
        raise IndexError('empty queue')
