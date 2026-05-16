class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = max(max(edge) for edge in edges) + 1
        parent = [i for i in range(n)]
        for edge in edges:
            n1 = edge[0]
            n2 = edge[1]
            if not self.union(n1, n2, parent):
                return edge

    def find(self, node: int, parent: List[int]) -> int:
        while parent[node] != node:
            node = parent[node]
        return node

    def union(self, n1: int, n2: int, parent: List[int]) -> bool:
        r1 = self.find(n1, parent)
        r2 = self.find(n2, parent)
        if r1 == r2:
            return False
        else:
            parent[r1] = r2
            return True