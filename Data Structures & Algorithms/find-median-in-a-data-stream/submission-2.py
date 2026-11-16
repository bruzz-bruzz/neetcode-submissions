class MedianFinder:

    def __init__(self):
        self.s = []

    def addNum(self, num: int) -> None:
        self.s.append(num)
    def findMedian(self) -> float:
        self.s.sort()
        n = len(self.s) // 2
        if len(self.s) % 2 == 0:
            return (self.s[n] + self.s[n - 1]) / 2
        else:
            return self.s[n]
        