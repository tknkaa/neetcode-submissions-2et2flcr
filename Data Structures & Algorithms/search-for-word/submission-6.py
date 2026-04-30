class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.height = len(board)
        self.width = len(board[0])
        self.board = board
        self.word = word
        self.found = False
        for i in range(0, self.height):
            for j in range(0, self.width):
                if self.found:
                    return True
                path = set()
                index = 0
                self.track(i, j, path, index)
        return self.found

    def track(self, i: int, j: int, path: Set[Tuple[int, int]], index: int):
        if self.found:
            return
        if index == len(self.word):
            self.found = True
            return
        if i < 0 or j < 0 or i >= self.height or j >= self.width:
            return
        if (i, j) in path:
            return
        if self.word[index] != self.board[i][j]:
            return

        path.add((i, j))
        self.track(i - 1, j, path, index + 1)
        self.track(i + 1, j, path, index + 1)
        self.track(i, j - 1, path, index + 1)
        self.track(i, j + 1, path, index + 1)
        path.remove((i, j))
