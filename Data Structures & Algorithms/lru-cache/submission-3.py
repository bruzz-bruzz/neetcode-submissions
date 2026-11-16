class LRUCache:

    def __init__(self, capacity: int):
        self.store = {}
        self.size = capacity
        self.used = []
    def get(self, key: int) -> int:
        if key in self.store.keys():
            if key in self.used:
                idx = self.used.index(key)
                self.used.pop(idx)
                self.used.append(key)
            else:
                self.used.append(key)
            return self.store[key]
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.used:
            idx = self.used.index(key)
            self.used.pop(idx)
            self.used.append(key)
        else:
            self.used.append(key)
        if key in self.store.keys():
            self.store[key] = value
        else:
            if len(self.store.keys()) + 1 <= self.size:
                self.store[key] = value
            else:
                del self.store[self.used.pop(0)]
                self.store[key] = value
