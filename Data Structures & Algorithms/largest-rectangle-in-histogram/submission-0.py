class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        right_boundary = [0] * n
        i = 0
        while i < n:
            if i == 0:
                stack.append((i, heights[i]))
            else:
                while stack and stack[-1][1] > heights[i]:
                    right_boundary[stack[-1][0]] = i
                    stack.pop()
                stack.append((i, heights[i]))
            i += 1
        while stack:
            right_boundary[stack[-1][0]] = n
            stack.pop()  

        print(right_boundary)
                
        stack = []
        left_boundary = [0] * n
        i = n - 1
        while i >= 0:
            if i == n - 1:
                stack.append((i, heights[i]))
            else:
                while stack and stack[-1][1] > heights[i]:
                    left_boundary[stack[-1][0]] = i
                    stack.pop()
                stack.append((i, heights[i]))
            i -= 1
        while stack:
            left_boundary[stack[-1][0]] = -1
            stack.pop()  

        print(left_boundary)
        area = [0] * n
        for i in range(n):
            area[i] = (right_boundary[i] - left_boundary[i] - 1) * heights[i]
        return max(area)
