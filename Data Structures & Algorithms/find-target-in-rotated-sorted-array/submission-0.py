class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minIndex = findMinIndex(nums)
        ascendingNums = nums
        if minIndex != 0:
            ascendingNums = nums[minIndex:] + nums[:minIndex]
        ng = -1
        ok = len(ascendingNums)
        while ok - ng > 1:
            mid = (ok + ng) // 2
            if ascendingNums[mid] >= target:
                ok = mid
            else:
                ng = mid
        if ok < len(ascendingNums) and ascendingNums[ok] == target:
            return (minIndex + ok) % len(ascendingNums)
        else:
            return -1

def findMinIndex(nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1
    if nums[left] < nums[right]:
        return left
    while right - left > 1:
        mid = (left + right) // 2
        if nums[mid] >= nums[right]:
            left = mid
        else:
            right = mid
    return right
        