class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m = len(nums1)
        n = len(nums2)
        half_size = (m + n) // 2
        is_even = (m + n) % 2 == 0

        ok = 0
        ng = m + 1
        while ng - ok > 1:
            x = (ok + ng) // 2
            if self.is_valid(x, half_size, nums1, nums2):
                ok = x
            else:
                ng = x
        
        x = ok
        max_left_short = nums1[x - 1] if x > 0 else float('-inf')
        min_right_short = nums1[x] if x < m else float('inf')
        max_left_long = nums2[half_size - x - 1] if half_size - x > 0 else float('-inf')
        min_right_long = nums2[half_size - x] if half_size - x < n else float('inf')

        if is_even:
            return (max(max_left_short, max_left_long) + min(min_right_short, min_right_long)) / 2
        else:
            return float(min(min_right_short, min_right_long))

    def is_valid(self, x: int, half_size: int, short: List[int], long: List[int]) -> bool:
        max_left_short = short[x - 1] if x > 0 else float('-inf')
        min_right_long = long[half_size - x] if half_size - x < len(long) else float('inf')
        return max_left_short <= min_right_long