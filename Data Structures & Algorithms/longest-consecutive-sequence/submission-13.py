class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        l = 0
        res = 0
        while l < len(nums):
            r = l + 1
            while r < len(nums):
                if nums[r] - nums[r-1] != 1:
                    break
                r += 1
            res = max(res,r - l)
            l = r
        return res