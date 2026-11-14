class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def qs(arr):
            if len(arr) > 1:
                p = arr[len(arr) // 2]
                l,r,m = [x for x in arr if x < p],[x for x in arr if x > p], [x for x in arr if x == p]
                return qs(l) + m + qs(r)
            return arr
        return qs(nums)