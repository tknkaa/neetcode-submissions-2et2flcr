class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area = self.dfs(r, c, grid, 0)
                    if area > max_area:
                        max_area = area
        return max_area
    def dfs(self, r, c, grid, area):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
            return area
        if grid[r][c] == 0:
            return area
        else:
            grid[r][c] = 0
            return 1 + self.dfs(r - 1, c, grid, area) + self.dfs(r + 1, c, grid, area) + self.dfs(r, c - 1, grid, area) + self.dfs(r, c + 1, grid, area)