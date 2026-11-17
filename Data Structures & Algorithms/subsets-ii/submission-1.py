class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        s = [[]]
        res = set()
        for n in nums:
            s += [sub + [n] for sub in s]
        for x in s:
            x.sort()
            res.add(tuple(x))
        return list(res)