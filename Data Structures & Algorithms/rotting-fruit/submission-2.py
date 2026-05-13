from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
        t = 0
        while q:
            l = len(q)
            for _ in range(l):
                r, c = q.popleft()
                if r - 1 >= 0 and grid[r - 1][c] == 1:
                    grid[r - 1][c] = 2
                    q.append((r - 1, c))
                if r + 1 < m and grid[r + 1][c] == 1:
                    grid[r + 1][c] = 2
                    q.append((r + 1, c))
                if c - 1 >= 0 and grid[r][c - 1] == 1:
                    grid[r][c - 1] = 2
                    q.append((r, c - 1))
                if c + 1 < n and grid[r][c + 1] == 1:
                    grid[r][c + 1] = 2
                    q.append((r, c + 1))
            t += 1
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    return -1
        return max(t - 1, 0)
