class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.result = []

        left_count = 0
        right_count = 0
        path = ""
        self.track(left_count, right_count, path)

        return self.result

    def track(self, left_count: int, right_count: int, path: str):
        if left_count == self.n:
            path += ")" * (2 * self.n - len(path))
            self.result.append(path)
        elif left_count < self.n and left_count == right_count:
            self.track(left_count + 1, right_count, path + "(")
        elif left_count < self.n and left_count > right_count:
            self.track(left_count + 1, right_count, path + "(")
            self.track(left_count, right_count + 1, path + ")")


        