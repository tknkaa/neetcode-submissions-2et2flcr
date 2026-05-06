class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)
        self.result = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                self.track(board, r, c, "")
        return list(set(self.result))
    
    def track(self, board: List[List[str]], r: int, c: int, word: str):
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
            return
        if board[r][c] == ".":
            return
        if not self.trie.starts_with(word):
            return
        prev = board[r][c]

        new_word = word + prev
        if self.trie.search(new_word):
            self.result.append(new_word)

        board[r][c] = "."
        self.track(board, r + 1, c, new_word)
        self.track(board, r - 1, c, new_word)
        self.track(board, r, c + 1, new_word)
        self.track(board, r, c - 1, new_word)
        board[r][c] = prev

        
class Trie:
    def __init__(self):
        self.root = {}
    def insert(self, word: str):
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node["#"] = True
    
    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        if "#" in node and node["#"]:
            return True
        else:
            return False
    
    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True