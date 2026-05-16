class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = n
        parent = [i for i in range(n)]
        for edge in edges:
            n1 = edge[0]
            n2 = edge[1]
            res -= self.union(n1, n2, parent)
        return res

    def find(self, node: int, parent: List[int]) -> int:
        while parent[node] != node:
            node = parent[node]
        return node

    def union(self, n1: int, n2: int, parent: List[int]) -> int:
        r1 = self.find(n1, parent)
        r2 = self.find(n2, parent)
        if r1 == r2:
            return 0
        else:
            parent[r2] = r1
            return 1