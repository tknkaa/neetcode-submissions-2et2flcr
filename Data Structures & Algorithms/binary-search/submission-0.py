class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ng = -1
        ok = len(nums)
        while ok - ng > 1:
            mid = (ng + ok) // 2
            if nums[mid] >= target:
                ok = mid
            else:
                ng = mid
        if ok < len(nums) and nums[ok] == target:
            return ok
        else:
            return -1