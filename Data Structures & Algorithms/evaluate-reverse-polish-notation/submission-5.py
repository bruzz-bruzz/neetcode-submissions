class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokens = deque(tokens)
        stk = []
        tok = '+-*/'
        while tokens:
            p = tokens.popleft()
            if p in tok:
                r,l = stk.pop(),stk.pop()
                if p == '+':
                    stk.append(l + r)
                if p == '-':
                    stk.append(l - r)
                if p == '*':
                    stk.append(l * r)
                if p == '/':
                    stk.append(int(l / r))
            else:
                stk.append(int(p))
        return stk[0]