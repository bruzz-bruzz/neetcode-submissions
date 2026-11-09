class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        c = 0
        for x in range(len(prices)):
            for y in range(x+1,len(prices)):
                c = max(c,prices[y] - prices[x])
        return c