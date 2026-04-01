from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = Counter(nums)
        i = 0
        count = 0
        tmp = 0
        while i < len(nums):
            num = nums[i]
            if counter[num - 1] == 0 and counter[num] >= 1:
                tmp = 1
                while counter[num + 1] >= 1:
                    num += 1
                    tmp += 1
            if tmp > count:
                count = tmp
            i += 1
        return count