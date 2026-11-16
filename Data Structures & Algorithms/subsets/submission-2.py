class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs = [[]]
        for num in nums:
            subs += [sub + [num] for sub in subs]
        return subs