class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        arr0 = nums[:-1]
        dp0 = [0] * len(arr0)
        dp0[0] = arr0[0]
        dp0[1] = max(arr0[0], arr0[1])
        for i in range(2, len(arr0)):
            dp0[i] = max(dp0[i - 2] + arr0[i], dp0[i - 1])
        arr1 = nums[1:]
        dp1 = [0] * len(arr1)
        dp1[0] = arr1[0]
        dp1[1] = max(arr1[0], arr1[1])
        for i in range(2, len(arr1)):
            dp1[i] = max(dp1[i - 2] + arr1[i], dp1[i - 1])
        return max(dp0[-1], dp1[-1])
        
    