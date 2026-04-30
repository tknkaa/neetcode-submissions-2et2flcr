class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.height = len(board)
        self.width = len(board[0])
        self.board = board
        self.word = word
        self.found = False
        for i in range(0, self.height):
            for j in range(0, self.width):
                path = []
                word = ""
                self.track(i, j, path, word)
        return self.found

    def track(self, i: int, j: int, path: List[Tuple[int, int]], word: str):
        if self.found:
            return
        if word == self.word:
            self.found = True
            return
        if i < 0 or j < 0 or i >= self.height or j >= self.width:
            return
        if (i, j) in path:
            return
        if len(word) == len(self.word):
            return

        path.append((i, j))
        word += self.board[i][j]
        self.track(i - 1, j, path, word)
        self.track(i + 1, j, path, word)
        self.track(i, j - 1, path, word)
        self.track(i, j + 1, path, word)
        path.pop()
        word = word[:-1]
