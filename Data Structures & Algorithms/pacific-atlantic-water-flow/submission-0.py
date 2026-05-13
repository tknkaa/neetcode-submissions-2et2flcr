class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        self.heights = heights
        self.pacific = set()
        self.atlantic = set()
        self.m = m
        self.n = n
        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    self.dfs_pacific(r, c)
                if r == m - 1 or c == n - 1:
                    self.dfs_atlantic(r, c)
        
        tuples = self.pacific & self.atlantic
        ans = []
        for t in tuples:
            ans.append(list(t))
        return ans

    def dfs_pacific(self, r: int, c: int):
        if (r, c) in self.pacific:
            return

        self.pacific.add((r, c))

        current = self.heights[r][c]

        if r - 1 >= 0 and self.heights[r - 1][c] >= current and (r - 1, c) not in self.pacific:
            self.dfs_pacific(r - 1, c)
        if r + 1 < self.m and self.heights[r + 1][c] >= current and (r + 1, c) not in self.pacific:
            self.dfs_pacific(r + 1, c)
        if c - 1 >= 0 and self.heights[r][c - 1] >= current and (r, c - 1) not in self.pacific:
            self.dfs_pacific(r, c - 1)
        if c + 1 < self.n and self.heights[r][c + 1] >= current and (r, c + 1) not in self.pacific:
            self.dfs_pacific(r, c + 1)
        return

    def dfs_atlantic(self, r: int, c: int):
        if (r, c) in self.atlantic:
            return
        
        self.atlantic.add((r, c))

        current = self.heights[r][c]

        if r - 1 >= 0 and self.heights[r - 1][c] >= current and (r - 1, c) not in self.atlantic:
            self.dfs_atlantic(r - 1, c)
        if r + 1 < self.m and self.heights[r + 1][c] >= current and (r + 1, c) not in self.atlantic:
            self.dfs_atlantic(r + 1, c)
        if c - 1 >= 0 and self.heights[r][c - 1] >= current and (r, c - 1) not in self.atlantic:
            self.dfs_atlantic(r, c - 1)
        if c + 1 < self.n and self.heights[r][c + 1] >= current and (r, c + 1) not in self.atlantic:
            self.dfs_atlantic(r, c + 1)
        return
