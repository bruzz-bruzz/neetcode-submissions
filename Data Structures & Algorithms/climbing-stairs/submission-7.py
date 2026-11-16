class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1,2,3]
        for x in range(2,n - 1):
            arr.append(arr[len(arr) - 2] + arr[len(arr) - 1])
        return arr[n - 1]