class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = []
        for x in range(len(nums)):
            if nums[x] == val:
                idx.append(x)
        while idx:
            p = idx.pop()
            nums.pop(p)
        return len(nums)