class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for x in nums:
            d[x] = 1 + d.get(x,0)
        ke = list(d.values())
        ke.sort(reverse=True)
        ke = ke[:k]
        res = []
        for x in d.keys():
            if d[x] in ke:
                res.append(x)
        return res