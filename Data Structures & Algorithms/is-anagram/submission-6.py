class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1,d2 = {},{}
        for x in s:
            d1[x] = 1 + d1.get(x,0)
        for x in t:
            d2[x] = 1 + d2.get(x,0)
        k = list(d1.keys())
        c = 0
        for x in k:
            if d1.get(x,0) == d2.get(x,0):
                c += 1
            else:
                return False
        k = list(d2.keys())
        c = 0
        for x in k:
            if d1.get(x,0) == d2.get(x,0):
                c += 1
            else:
                return False
        return True