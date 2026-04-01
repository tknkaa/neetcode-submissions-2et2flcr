from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymap = defaultdict(int)
        i = 0
        j = 0
        while i < len(nums):
            diff = target - nums[i]
            if diff not in mymap.keys():
                mymap[nums[i]] = i
            else:
                j = mymap[diff]
                break
            i += 1
        return [j, i]
