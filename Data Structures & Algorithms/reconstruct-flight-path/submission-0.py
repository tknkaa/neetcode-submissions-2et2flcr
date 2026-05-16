from collections import defaultdict
import heapq
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.adj = defaultdict(list)
        for start, end in tickets:
            heapq.heappush(self.adj[start], end)
        self.res = []
        self.dfs("JFK")
        return self.res[::-1]

    def dfs(self, node: int):
        while self.adj[node]:
            neighbor = heapq.heappop(self.adj[node])
            self.dfs(neighbor)
        self.res.append(node)



        