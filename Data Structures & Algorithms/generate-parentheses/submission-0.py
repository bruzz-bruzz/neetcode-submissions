class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def recur(s,n,o,c):
            if len(s) >= n * 2:
                res.append(s)
            else:
                if o < n:
                    recur(s + '(',n,o + 1,c)
                if c < n:
                    if o > c:
                        recur(s + ')',n,o,c + 1)
        recur('(',n,1,0)
        return res