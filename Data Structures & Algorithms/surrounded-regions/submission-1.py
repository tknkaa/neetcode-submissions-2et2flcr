class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        self.m = m
        self.n = n
        self.board = board
        for r in range(m):
            for c in range(n):
                if (r == 0 or r == m - 1 or c == 0 or c == n - 1) and board[r][c] == "O":
                    self.dfs(r, c)
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
        

    def dfs(self, r: int, c: int):
        self.board[r][c] = "#"
        if r - 1 >= 0 and self.board[r - 1][c] == "O":
            self.dfs(r - 1, c)
        if r + 1 < self.m and self.board[r + 1][c] == "O":
            self.dfs(r + 1, c)
        if c - 1 >= 0 and self.board[r][c - 1] == "O":
            self.dfs(r, c - 1)
        if c + 1 < self.n and self.board[r][c + 1] == "O":
            self.dfs(r, c + 1)
        return