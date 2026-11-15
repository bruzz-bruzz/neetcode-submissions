class TimeMap:

    def __init__(self):
        self.d = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if timestamp in self.d[key]:
            return self.d[key][timestamp]
        r = timestamp
        while r >= 0:
            if r in self.d[key]:
                return self.d[key][r]
            r -= 1
        return ''