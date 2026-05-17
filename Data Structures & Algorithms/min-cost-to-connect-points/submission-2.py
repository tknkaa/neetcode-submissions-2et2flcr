import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                a = points[i]
                b = points[j]
                weight = abs(a[0] - b[0]) + abs(a[1] - b[1])
                edges.append((weight, i, j))
        edges.sort(key = lambda edge: edge[0])

        cost = 0
        parent = [i for i in range(len(points))]
        edge_count = 0
        for edge in edges:
            weight = edge[0]
            i = edge[1]
            j = edge[2]
            if self.union(i, j, parent):
                cost += weight
                edge_count += 1
                if edge_count == len(points) - 1:
                    break
        return cost


    def find(self, node: int, parent: List[int]) -> int:
        while node != parent[node]:
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