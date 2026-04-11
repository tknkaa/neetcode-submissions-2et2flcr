import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        small = []
        for point in points:
            dist = - (point[0]**2 + point[1]**2)
            heapq.heappush(small, (dist, point[0], point[1]))
            if len(small) > k:
                heapq.heappop(small)
        return list(map(lambda x: [x[1], x[2]], small))