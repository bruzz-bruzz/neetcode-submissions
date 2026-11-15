class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        while l ** 2 < x:
            l += 1
        if l ** 2 > x:
            return l - 1
        return l