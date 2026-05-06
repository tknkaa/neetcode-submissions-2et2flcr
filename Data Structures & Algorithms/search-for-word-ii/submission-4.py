class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = {}
        for word in words:
            node = self.root
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node["#"] = word
        self.board = board
        self.result = []
        node = self.root
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                self.track(r, c, node)
        return self.result

    def track(self, r: int, c: int, node):
        if r < 0 or c < 0 or r >= len(self.board) or c >= len(self.board[0]):
            return
        ch = self.board[r][c]
        if ch == "." or ch not in node:
            return
        next_node = node[ch]
        if "#" in next_node:
            self.result.append(next_node["#"])
            del next_node["#"]
        self.board[r][c] = "."
        self.track(r - 1, c, next_node)
        self.track(r + 1, c, next_node)
        self.track(r, c + 1, next_node)
        self.track(r, c - 1, next_node)
        self.board[r][c] = ch
        
        
