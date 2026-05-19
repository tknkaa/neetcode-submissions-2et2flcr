from collections import defaultdict

class Solution:
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        self.memos = defaultdict(int)
        return self.dfs(0)

    def dfs(self, i: int) -> int:
        if i >= len(self.nums):
            return 0
        if i in self.memos:
            return self.memos[i]
        else:
            v = max(self.nums[i] + self.dfs(i + 2), self.dfs(i + 1))
            self.memos[i] = v
            return v