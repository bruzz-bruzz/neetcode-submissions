class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        n = columnNumber
        while n > 0:
            stk = deque([[n,0]])
            while stk:
                p = stk.popleft()
                if p[0] > 26:
                    stk.append([p[0] // 26,p[1] + 1])
                else:
                    res.append(chr(p[0] + 64))
                    n -= p[0] * (26** p[1])
        return ''.join(res)