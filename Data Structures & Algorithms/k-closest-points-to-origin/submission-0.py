import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = list(map(lambda x: (x[0]**2 + x[1]**2, x[0], x[1]), points))
        heapq.heapify(points)
        small = []
        for _ in range(k):
            point = heapq.heappop(points)
            small.append([point[1], point[2]])
        return small