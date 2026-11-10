class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1 = sorted(s1)
        while l < len(s2) - len(s1) + 1:
            r = s2[l:l+len(s1)]
            if sorted(r) == s1:
                return True
            l += 1
        return False