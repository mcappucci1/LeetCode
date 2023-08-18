class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_elem = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, min_elem))

    def pop(self) -> None:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()