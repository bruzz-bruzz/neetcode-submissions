class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        c = 0
        for x in range(m,m + n):
            nums1[x] = nums2[c]
            c += 1
        nums1.sort()
        return nums1