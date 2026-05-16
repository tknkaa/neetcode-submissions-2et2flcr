import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        
        heap = [(0, k)] # time, node
        visited = set()

        res = 0

        while heap:
            time, nearest = heapq.heappop(heap)
            if nearest in visited:
                continue
            visited.add(nearest)
            res = max(res, time)

            for node, weight in adj[nearest]:
                if node not in visited:
                    heapq.heappush(heap, (time + weight, node))

        if len(visited) == n:
            return res
        else:
            return -1
        

