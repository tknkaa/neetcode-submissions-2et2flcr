class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        i = 0
        ans = []
        while i < len(sorted_nums) - 2:
            if i > 0 and sorted_nums[i - 1] == sorted_nums[i]:
                i += 1
                continue
            remains = sorted_nums[(i + 1):]
            first = sorted_nums[i]
            pairs = find_pairs(first, remains)
            for pair in pairs:
                ans.append(pair + [first])
            i += 1
        return ans


def find_pairs(first: int, remains: List[int]) -> List[List[int]]:
    l = 0
    r = len(remains) - 1
    ans = []
    while l < r:
        if remains[l] + remains[r] + first == 0:
            ans.append([remains[l],  remains[r]])
            while remains[l] == remains[l + 1]:
                l += 1
                if l == len(remains) - 1:
                    break
            while remains[r] == remains[r - 1]:
                r -= 1
                if r == 0:
                    break
            r -= 1
        elif remains[l] + remains[r] + first < 0:
            l += 1
        else:
            r -= 1
    return ans