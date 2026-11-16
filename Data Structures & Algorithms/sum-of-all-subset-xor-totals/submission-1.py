class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def xor(arr):
            l = arr[0] if arr else 0
            for x in range(1,len(arr)):
                l ^= arr[x]
            return l
        subs = [[]]
        for n in nums:
            subs += [sub + [n] for sub in subs]
        c = 0
        for x in subs:
            c += xor(x)
        return c
