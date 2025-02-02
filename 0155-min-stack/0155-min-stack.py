class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = 0

    def push(self, val: int) -> None:
        if not self.stack:
            self.minVal = val
        self.minVal = min(self.minVal, val)
        self.stack.append((val, self.minVal))
        

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.minVal = self.stack[-1][1]
        

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