class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0,1,1]
        for x in range(2,n):
            arr.append(arr[len(arr) - 1] + arr[len(arr) - 2] + arr[len(arr) - 3])
        return arr[n]