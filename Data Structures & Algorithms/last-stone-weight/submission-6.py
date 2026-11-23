class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) < 2:
            return stones.pop()
        s = [-x for x in stones]
        heapq.heapify(s)
        while len(s) >= 2:
            l,r = abs(heapq.heappop(s)), abs(heapq.heappop(s))
            if l == r:
                pass
            elif l < r or l > r:
                heapq.heappush(s,-abs(l - r))
        return abs(heapq.heappop(s)) if s else 0