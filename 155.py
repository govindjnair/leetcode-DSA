class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = float("inf")

    def push(self, val: int) -> None:
        if val < self.minVal:
            self.minVal = val
        self.stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.minVal:
            if self.stack:
                self.minVal = min(self.stack)
            else:
                self.minVal = float("inf")

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return int(self.minVal)


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
print(None)
print(obj.push(val=2147483646))
print(obj.push(val=2147483646))
print(obj.push(val=2147483647))
param_3 = obj.top()
print(param_3)
print(obj.pop())
a = obj.getMin()
print(a)
print(obj.pop())
b = obj.getMin()
print(b)
print(obj.pop())
print(obj.push(val=2147483647))
c = obj.top()
print(c)
d = obj.getMin()
print(d)
obj.push(val=-2147483648)
e = obj.top()
print(e)
f = obj.getMin()
print(f)
print(obj.pop())
g = obj.getMin()
print(g)


class MinStack2:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minStack:
            self.minStack.append(val)
        elif self.minStack[-1] < val:
            self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
