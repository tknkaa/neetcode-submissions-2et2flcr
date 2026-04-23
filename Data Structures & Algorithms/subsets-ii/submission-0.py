class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        path = []
        self.nums = sorted(nums)
        self.track(path, 0)
        return self.result
        
    def track(self, path: List[int], index: int):
        print(path, index)
        if index == len(self.nums):
            self.result.append(path[:])
            return
        path.append(self.nums[index])
        self.track(path, index + 1)
        path.pop()
        while index < len(self.nums) - 1 and self.nums[index] == self.nums[index + 1]:
            index += 1
        self.track(path, index + 1)