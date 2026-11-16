class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for x in digits:
            s += str(x)
        s = int(s)
        s += 1
        res = []
        for x in str(s):
            res.append(int(x))
        return res