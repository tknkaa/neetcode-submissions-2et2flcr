class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        self.s = s

        start = 0
        end = 1
        path = []

        self.backtrack(start, end, path)

        return self.result

    def backtrack(self, start: int, end: int, path: List[str]):
        if start == len(self.s) and end == len(self.s) + 1:
            self.result.append(path[:])
            return
        elif start >= len(self.s) or end > len(self.s):
            return

        word = self.s[start:end]
        print(word)

        if self.palindrome(word):
            path.append(word)
            self.backtrack(end, end + 1, path)
            path.pop()
        
        end = end + 1
        self.backtrack(start, end, path)

    def palindrome(self, word: str) -> bool:
        l = len(word)
        for i in range(int(l/2)):
            if word[i] != word[l - i - 1]:
                return False
        return True
        
        