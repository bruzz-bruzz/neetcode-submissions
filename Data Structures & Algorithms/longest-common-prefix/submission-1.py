class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        l = 0
        m = strs[0]
        while l < len(m):
            c = 1
            s = strs[0][:l + 1]
            for x in range(1,len(strs)):
                if s == strs[x][:l + 1]:
                    c += 1
            if c == len(strs):
                l += 1
            else:
                return s[:len(s) - 1]
        return strs[0][:l + 1]