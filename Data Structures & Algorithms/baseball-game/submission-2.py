class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = '+DC'
        stk = []
        ops = deque(operations)
        while ops:
            p = ops.popleft()
            if p in s:    
                if p == '+':
                    l,r = stk.pop(),stk.pop()
                    stk.append(r)
                    stk.append(l)
                    stk.append(l + r)
                elif p == 'D':
                    l = stk.pop()
                    stk.append(l)
                    stk.append(l * 2)
                else:
                    stk.pop()
            else:
                stk.append(int(p))
        return sum(stk)