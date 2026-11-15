class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for x in range(n):
            for y in range(x+1,n):
                if nums[x] == nums[y] and abs(x - y) <= k:
                    return True
        return False