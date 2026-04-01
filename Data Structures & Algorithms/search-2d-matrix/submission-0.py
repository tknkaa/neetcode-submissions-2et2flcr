class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []
        for row in matrix:
            nums += row
        ng = -1
        ok = len(nums)
        while ok - ng > 1:
            mid = (ng + ok)//2
            if nums[mid] >= target:
                ok = mid
            else:
                ng = mid
        if ok < len(nums) and nums[ok] == target:
            return True
        else:
            return False