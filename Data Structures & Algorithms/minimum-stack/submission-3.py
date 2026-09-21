class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')
        

    def push(self, val: int) -> None:
        self.min = min(val, self.min)
        self.stack.append((val, self.min))        

    def pop(self) -> None:
        if not self.stack:
            return

        self.stack.pop()
        if self.stack:
            self.min = self.stack[-1][1]
        else:
            self.min = float('inf')
        
        

    def top(self) -> int:
        if not self.stack:
            return None

        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.min

        
