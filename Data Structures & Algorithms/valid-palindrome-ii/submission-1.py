class Solution:
    def validPalindrome(self, s: str) -> bool:
        def pal(st):
            l,r = 0, len(st) - 1
            while l < r:
                if st[l] != st[r]:
                    return False
                l += 1
                r -= 1
            return True
        s = list(s)
        for x in range(len(s)):
            n = s[:]
            n.pop(x)
            if pal(n) == True:
                return True
        return False