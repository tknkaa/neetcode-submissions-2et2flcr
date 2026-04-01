import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_nums = []
        window = []
        for i in range(0, k):
            heapq.heappush(window, (-nums[i], i))
        l = 0
        while l < len(nums) - k + 1:
            max_nums.append(-window[0][0])
            if l < len(nums) - k :
                heapq.heappush(window, (-nums[l + k], l + k))
            max_index = window[0][1]
            while len(window) > 0 and max_index <= l:
                heapq.heappop(window)
                if len(window) > 0:
                    max_index = window[0][1]
            l += 1
        return max_nums