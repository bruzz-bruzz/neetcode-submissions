class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        for x in nums:
            d[x] = 1 + d.get(x,0)
        arr = []
        n = len(nums) / 3
        for x in d:
            if d[x] > n:
                arr.append(x)
        return arr