from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2**31 - 1
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            if c - 1 >= 0 and grid[r][c - 1] == inf:
                grid[r][c - 1] = grid[r][c] + 1
                queue.append((r, c - 1))
            if c + 1 < n and grid[r][c + 1] == inf:
                grid[r][c + 1] = grid[r][c] + 1
                queue.append((r, c + 1))
            if r - 1 >= 0 and grid[r - 1][c] == inf:
                grid[r - 1][c] = grid[r][c] + 1
                queue.append((r - 1, c))
            if r + 1  < m and grid[r + 1][c] == inf:
                grid[r + 1][c] = grid[r][c] + 1
                queue.append((r + 1, c))
        