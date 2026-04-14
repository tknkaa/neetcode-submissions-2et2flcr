class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.results = []
        temp = []
        self.backtrack(0, temp)
        return self.results
    def backtrack(self, i: int, temp: List[int]):
        if i == len(self.nums):
            self.results.append(temp[:])
            return
        temp.append(self.nums[i])
        self.backtrack(i + 1, temp)
        temp.pop()
        self.backtrack(i + 1, temp)