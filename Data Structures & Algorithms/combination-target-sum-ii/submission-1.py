class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = sorted(candidates)
        self.target = target
        self.result: List[List[int]] = []
        path = []
        self.track(0, path, 0)
        return self.result

    def track(self, start: int, path: List[int], path_sum: int):
        if path_sum == self.target:
            print(path)
            self.result.append(path[:])
            return

        elif path_sum > self.target:
            return

        for i in range(start, len(self.candidates)):
            if i > start and self.candidates[i - 1] == self.candidates[i]:
                continue
            path.append(self.candidates[i])
            self.track(i + 1, path, path_sum + self.candidates[i])
            path.pop()