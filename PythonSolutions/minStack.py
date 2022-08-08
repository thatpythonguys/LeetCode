class MinStack:
    # To keep track of our minimums, we implement a separate minimum stack, that keeps track of the minimum for our actual stack.
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        if not self.stack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(self.minStack[-1], val))
        self.stack.append(val)

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
