class Solution:
    my_map = {
        2: ["a", "b", "c"],
        3: ["d", "e", "f"],
        4: ["g", "h", "i"],
        5: ["j", "k", "l"],
        6: ["m", "n", "o"],
        7: ["p", "q", "r", "s"],
        8: ["t", "u", "v"],
        9: ["w", "x", "y", "z"]
    }
    def letterCombinations(self, digits: str) -> List[str]:
        self.result = []
        self.digits = list(map(int, list(digits)))
        print(self.digits)
        path = []
        index = 0
        self.backtrack(index, path)
        return self.result

    def backtrack(self, index: int, path: List[str]):
        if index == len(self.digits):
            if len(path) > 0:
                self.result.append("".join(path))
            return
        for ch in self.my_map[self.digits[index]]:
            path.append(ch)
            self.backtrack(index + 1, path)
            path.pop()