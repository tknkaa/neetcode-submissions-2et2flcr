class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        area = min(heights[l], heights[r]) * (r - l)
        while l < r:
            tmp = min(heights[l], heights[r]) * (r - l)
            if area < tmp:
                area = tmp
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return area

        