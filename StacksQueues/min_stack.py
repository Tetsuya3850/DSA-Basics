
class Min_Stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def isEmpty(self):
        return not (self.stack or self.min_stack)

    def push(self, value):
        if self.isEmpty():
            self.min_stack.append(value)
        else:
            last_min = self.min()
            if value < last_min:
                self.min_stack.append(value)
        self.stack.append(value)

    def pop(self):
        if self.isEmpty():
            return False
        else:
            pop_value = self.stack.pop()
            if pop_value == self.min():
                self.min_stack.pop()

    def min(self):
        return self.min_stack[-1]

    def peek(self):
        return self.stack[-1]


min_stack = Min_Stack()
min_stack.push(6)
min_stack.push(3)
min_stack.push(4)
min_stack.push(9)
min_stack.push(2)
min_stack.pop()
print(min_stack.min())
