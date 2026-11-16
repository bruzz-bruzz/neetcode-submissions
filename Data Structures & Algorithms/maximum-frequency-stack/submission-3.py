class FreqStack:

    def __init__(self):
        self.s = []
        self.d = {}
    def push(self, val: int) -> None:
        self.s.append(val)
        self.d[val] = 1 + self.d.get(val,0)
    def pop(self) -> int:
        m = max(self.d.values())
        arr = []
        r = len(self.s) - 1
        while r >= 0:
            if self.d[self.s[r]] == m:
                n = self.s[r]
                self.d[self.s[r]] = -1 + self.d.get(self.s[r],0)
                self.s.pop(r)
                return n
            r -= 1
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()