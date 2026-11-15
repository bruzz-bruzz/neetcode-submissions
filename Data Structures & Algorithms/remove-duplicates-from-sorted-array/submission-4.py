class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = []
        s = set()
        for x in range(len(nums)):
            if nums[x] in s:
                idx.append(x)
            s.add(nums[x])
        while idx:
            p = idx.pop()
            nums.pop(p)
        return len(nums)