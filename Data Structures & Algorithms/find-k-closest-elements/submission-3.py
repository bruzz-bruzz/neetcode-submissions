class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr):
            return arr
        d = defaultdict(list)
        for y in arr:
            res = abs(x-y)
            d[res].append(y)
        alll = []
        ke = list(d.keys())
        ke.sort()
        for y in ke:
            for z in d[y]:
                alll.append(z)
        alll = alll[:k]
        alll.sort()
        return alll