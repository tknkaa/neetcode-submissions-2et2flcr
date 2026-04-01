class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack: Tuple[int, int] = [] #index, temperature
        result = [0] * len(temperatures)
        i = 0
        while i < len(temperatures):
            if i == 0:
                stack.append((0, temperatures[i]))
            elif stack[-1][1] >= temperatures[i]:
                stack.append((i, temperatures[i]))
            else:
                while stack and stack[-1][1] < temperatures[i]:
                    result[stack[-1][0]] = i - stack[-1][0]
                    stack.pop()
                stack.append((i, temperatures[i]))
            i += 1
        return result