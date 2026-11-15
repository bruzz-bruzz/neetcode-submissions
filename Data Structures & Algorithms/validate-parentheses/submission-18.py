class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        d = {
            '}':"{",
            ']':"[",
            ')':"("
        }
        stk = []
        l = 0
        c = 0
        while l < len(s):
            if s[l] in d.keys():
                if stk:
                    if stk.pop() == d[s[l]]:
                        c += 1
                else:
                    return False
            else:   
                stk.append(s[l])
            l += 1
        return c == len(s) // 2