class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.nums = nums
        self.target = target
        self.result = []
        path = []
        self.track(0, path, 0)
        return self.result

    def track(self, start: int, path: List[int], current_sum: int):
        if current_sum == self.target:
            self.result.append(path[:])
            return 
        elif current_sum > self.target:
            return 
        for i in range(start, len(self.nums)):
            path.append(self.nums[i])
            self.track(i, path, current_sum + self.nums[i])
            path.pop()