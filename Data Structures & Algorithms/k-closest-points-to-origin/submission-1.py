class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(arr):
            return math.sqrt((arr[0] ** 2) + (arr[1] ** 2))
        d = defaultdict(list)
        for x in points:
            d[dist(x)].append(x)
        m = list(d.keys())
        m.sort()
        res = []
        for x in m:
            for y in d[x]:
                res.append(y)
        return res[:k]