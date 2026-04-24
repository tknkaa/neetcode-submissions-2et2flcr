class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.result = []

        left_count = 0
        right_count = 0
        path = []
        self.track(left_count, right_count, path)

        return self.result

    def track(self, left_count: int, right_count: int, path: List[str]):
        if len(path) == 2 * self.n:
            self.result.append("".join(path))
        if left_count < self.n:
            path.append("(")
            self.track(left_count + 1, right_count, path)
            path.pop()
        if left_count > right_count:
            path.append(")")
            self.track(left_count, right_count + 1, path)
            path.pop()


        