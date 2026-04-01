class MinStack:

    def __init__(self):
        self.stack = []
        self.extra = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.extra) == 0:
            self.extra.append(val)
        else:
            self.extra.append(min(self.extra[-1], val))

    def pop(self) -> None:
        self.stack = self.stack[:len(self.stack) - 1]
        self.extra = self.extra[:len(self.extra) - 1]
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.extra[-1]