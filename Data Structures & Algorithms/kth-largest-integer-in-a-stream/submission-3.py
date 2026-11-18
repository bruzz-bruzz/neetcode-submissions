class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.s = nums
        self.k = k
    def add(self, val: int) -> int:
        self.s.append(val)
        self.s.sort()
        return self.s[len(self.s) - self.k]
