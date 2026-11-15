class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for x in matrix:
            l,r = 0, len(x) - 1
            while l <= r:
                m = (l + r) // 2
                if x[m] == target:
                    return True
                elif x[m] < target:
                    l = m + 1
                else:
                    r = m - 1
        return False