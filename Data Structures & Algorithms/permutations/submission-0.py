class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        self.n = n
        self.nums = nums
        self.result = []

        path = []
        used = [False] * n
        self.track(path, used)
        return self.result
    def track(self, path: List[int], used: List[bool]):
        if len(path) == self.n:
            self.result.append(path[:])
            return
        for i in range(self.n):
            if not used[i]:
                path.append(self.nums[i])
                used[i] = True
                self.track(path, used)
                path.pop()
                used[i] = False