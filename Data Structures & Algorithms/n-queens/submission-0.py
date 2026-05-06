class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result: List[List[str]] = []
        self.n = n
        board = ["." * n for _ in range(n)]
        c = 0
        self.track(c, board)
        return self.result

    def track(self, c: int, board: List[str]):
        if c == self.n:
            self.result.append(board[:])
            return
        for r in range(self.n):
            if self.is_cell_suitable(r, c, board):
                board[r] = board[r][:c] + "Q" + board[r][c+1:]
                self.track(c + 1, board)
                board[r] = board[r][:c] + "." + board[r][c+1:]


    def is_cell_suitable(self, r: int, c: int, board: List[str]) -> bool:
        i = 1
        while r - i >= 0 and c - i >= 0:
            if board[r - i][c - i] == "Q":
                return False
            i += 1
        
        i = 1
        while r + i < self.n and c - i >= 0:
            if board[r + i][c - i] == "Q":
                return False
            i += 1
        
        if "Q" in board[r][:c]:
            return False

        i = 1

        while r - i >= 0:
            if board[r - i][c] == "Q":
                return False
            i += 1
    

        return True