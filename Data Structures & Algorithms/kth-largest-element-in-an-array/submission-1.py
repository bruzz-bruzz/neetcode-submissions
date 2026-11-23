class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        l = 0
        while len(nums) >= k:
            l = heapq.heappop(nums)
        return l