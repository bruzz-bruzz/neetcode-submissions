class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        l = 0
        res = 0
        while l < len(s):
            sett.add(s[l])
            r = l + 1
            while r < len(s):
                if s[r] in sett:
                    res = max(res, r - l)
                    while s[r] in sett:
                        sett.remove(s[l])
                        l += 1
                else:
                    sett.add(s[r])
                    r += 1
            l = r
        return max(res,len(sett))