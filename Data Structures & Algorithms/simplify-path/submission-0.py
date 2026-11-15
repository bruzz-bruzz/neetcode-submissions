class Solution:
    def simplifyPath(self, path: str) -> str:
        from collections import deque
        l = 0
        res = []
        stk = deque([])
        stk2 = []
        specs = ['.','..']
        for r in range(1,len(path)):
            if path[l] == '/' and path[r] == '/':
                sc = path[l + 1:r]
                if sc.count('/') != len(sc):
                    stk.append(path[l +1:r])
                l = r
        if path[len(path) - 1] != '/':
            stk.append(path[l + 1:])
        while stk:
            p = stk.popleft()
            if p in specs:
                if p == '.':
                    pass
                elif p == '..':
                    if res:
                        res.pop()
            else:
                res.append(p)
            stk2.append(p)
        return '/' + '/'.join(res)