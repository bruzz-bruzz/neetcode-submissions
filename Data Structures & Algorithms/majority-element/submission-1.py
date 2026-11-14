class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for x in nums:
            d[x] = 1 + d.get(x,0)
        for x in d.keys():
            if d[x] > len(nums) / 2:
                return x