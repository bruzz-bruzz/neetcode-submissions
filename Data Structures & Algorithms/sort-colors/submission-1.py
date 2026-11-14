class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def qs(arr):
            if len(arr) > 1:
                p = arr[len(arr) // 2]
                l,r,m = [x for x in arr if x < p],[x for x in arr if x > p], [x for x in arr if x == p]
                return qs(l) + m + qs(r)
            return arr
        a = qs(nums)
        for x in range(len(nums)):
            nums[x] = a[x]