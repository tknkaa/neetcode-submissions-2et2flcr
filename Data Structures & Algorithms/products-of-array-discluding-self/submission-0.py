class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        i = 0
        while i < len(nums):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = prefix[i - 1] * nums[i]
            i += 1
        suffix = [0] * len(nums)
        i = len(nums) - 1
        while i >= 0:
            if i == len(nums) - 1:
                suffix[i] = nums[i]
            else:
                suffix[i] = suffix[i + 1] * nums[i]
            i -= 1
        ans = [0] * len(nums)
        i = 0
        while i < len(nums):
            if i == 0:
                ans[i] = suffix[i + 1]
            elif i == len(nums) - 1:
                ans[i] = prefix[i - 1]
            else:
                ans[i] = prefix[i - 1] * suffix[i + 1]
            i += 1
        return ans