class MinStack:

    def __init__(self):
        self.obj = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.obj.append(val)
        if not self.minStack or val < self.obj[self.minStack[-1]]:
            self.minStack.append(len(self.obj) - 1) 
        else:
            self.minStack.append(self.minStack[-1])
            

    def pop(self) -> None:
        self.obj.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.obj[-1]

    def getMin(self) -> int:
        return self.obj[self.minStack[-1]]
