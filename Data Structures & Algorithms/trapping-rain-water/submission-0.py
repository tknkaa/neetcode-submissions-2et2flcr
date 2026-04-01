class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        i = 0
        while i < len(height):
            if i == 0:
                prefix[i] = height[i]
            else:
                prefix[i] = max(height[i], prefix[i - 1])
            i += 1
        suffix = [0] * len(height)
        i = len(height) - 1
        while i >= 0:
            if i == len(height) - 1:
                suffix[i] = height[len(height) - 1]
            else:
                suffix[i] = max(suffix[i + 1], height[i])
            i -= 1
        water = [0] * len(height)
        i = 1
        while i < len(height) - 1:
            water[i] = max(0, min(prefix[i - 1], suffix[i + 1]) - height[i])
            i += 1
        return sum(water)
