class MyCircularQueue:

    def __init__(self, k: int):
        self.s = []
        self.k = k

    def enQueue(self, value: int) -> bool:
        if len(self.s) + 1 <= self.k:
            self.s.append(value)
            return True
        return False

    def deQueue(self) -> bool:
        if self.s:
            self.s.pop(0)
            return True
        return False

    def Front(self) -> int:
        return self.s[0] if self.s else -1        

    def Rear(self) -> int:
        return self.s[len(self.s) - 1] if self.s else -1    

    def isEmpty(self) -> bool:
        return len(self.s) == 0

    def isFull(self) -> bool:
        return len(self.s) == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()