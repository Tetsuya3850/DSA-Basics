# Implement a queue with two stacks


class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, value):
        # Time O(1), Space O(1), where N is the length Queue.
        self.enqueue_stack.append(value)

    def dequeue(self):
        # Time O(1), Space O(1), where N is the length Queue.
        self.shift_stack()
        return self.dequeue_stack.pop()

    def shift_stack(self):
        # Time O(k), Space O(1), where k is the length of enqueue_stack.
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())


queue = Queue()
queue.enqueue(3)
queue.enqueue(2)
queue.enqueue(4)
print(queue.enqueue_stack)
queue.dequeue()
queue.dequeue()
print(queue.dequeue_stack)
