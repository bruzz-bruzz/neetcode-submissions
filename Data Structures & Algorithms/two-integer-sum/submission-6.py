class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for x in range(len(nums)):
            t = target - nums[x]
            if t in d.keys():
                return [d[t],x]
            d[nums[x]] = x