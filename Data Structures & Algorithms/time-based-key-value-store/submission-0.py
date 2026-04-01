from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list[tuple[int, str]])
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.map[key]
        n = len(pairs)
        if n == 0:
            return ""
        ok = -1
        ng = n
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if pairs[mid][0] <= timestamp:
                ok = mid
            else:
                ng = mid
        return pairs[ok][1] if ok != -1 else ""
