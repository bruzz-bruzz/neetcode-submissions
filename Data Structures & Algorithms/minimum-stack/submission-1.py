class MinStack:

    def __init__(self):
        self.d = []
        self.t = 0
        self.m = float("inf")
    def push(self, val: int) -> None:
        self.d.append(val)
        self.t = val
        if val < self.m:
            self.m = val
    def pop(self) -> None:
        self.d.pop()
    def top(self) -> int:
        return self.d[len(self.d) - 1]
    def getMin(self) -> int:
        return min(self.d) 
    