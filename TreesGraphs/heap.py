class MinHeap:
    def __init__(self):
        self.heap = []

    def peek(self):
        if not self.heap:
            return False
        return self.heap[0]

    def push(self, data):
        self.heap.append(data)
        self.heapify_up()

    def heapify_up(self):
        child = len(self.heap) - 1
        parent = (child - 1) // 2
        while self.heap[child] < self.heap[parent] and child != 0:
            self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child]
            child = parent
            parent = (child - 1) // 2

    def pop(self):
        if not self.heap:
            return False
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        data = self.heap.pop()
        self.heapify_down()
        return data

    def heapify_down(self):
        i = 0
        while (2*i+1) < len(self.heap):
            smaller_idx = 2*i+1
            if (2*i+2) < len(self.heap) and self.heap[2*i+2] < self.heap[2*i+1]:
                smaller_idx = 2*i+2
            if self.heap[smaller_idx] > self.heap[i]:
                return
            self.heap[smaller_idx], self.heap[i] = self.heap[i], self.heap[smaller_idx]
            i = smaller_idx

min_heap = MinHeap()
min_heap.push(5)
min_heap.push(3)
min_heap.push(9)
min_heap.push(4)
min_heap.pop()
print (min_heap.heap)
