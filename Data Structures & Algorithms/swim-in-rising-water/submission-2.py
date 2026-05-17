import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        path = []
        path.append((grid[0][0], 0, 0))

        while path:
            current_elevation, i, j = heapq.heappop(path)
            if (i, j) in visited:
                continue

            visited.add((i, j))
            if i == n - 1 and j == n - 1:
                return current_elevation

            neighbors = []

            if i + 1 < n:
                neighbors.append((grid[i + 1][j], i + 1, j))
            if j + 1 < n:
                neighbors.append((grid[i][j + 1], i, j + 1))
            if j - 1 >= 0:
                neighbors.append((grid[i][j - 1], i, j - 1))
            if i - 1 >= 0:
                neighbors.append((grid[i - 1][j], i - 1, j))
            for neighbor in neighbors:
                elevation = neighbor[0]
                i = neighbor[1]
                j = neighbor[2]
                heapq.heappush(path, (max(current_elevation, elevation), i, j))

