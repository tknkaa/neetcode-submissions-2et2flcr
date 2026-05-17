import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        path = []
        path.append((grid[0][0], 0, 0))
        current_cost = grid[0][0]

        while path:
            elevation, i, j = heapq.heappop(path)
            current_cost = max(current_cost, elevation)
            if (i, j) in visited:
                continue
            if i == n - 1 and j == n - 1:
                break

            visited.add((i, j))

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
                heapq.heappush(path, (elevation, i, j))
        return current_cost

