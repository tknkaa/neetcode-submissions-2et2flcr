class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i = 0
        while i < len(tokens):
            result = 0
            if tokens[i] == "+":
                result = stack[-2] + stack[-1]
                stack = stack[:len(stack) - 2] + [result]
            elif tokens[i] == "-":
                result = stack[-2] - stack[-1]
                stack = stack[:len(stack) - 2] + [result]
            elif tokens[i] == "*":
                result = stack[-2] * stack[-1]
                stack = stack[:len(stack) - 2] + [result]
            elif tokens[i] == "/":
                result = int(stack[-2] / stack[-1])
                stack = stack[:len(stack) - 2] + [result]
            else:
                stack.append(int(tokens[i]))
            i += 1
        return stack[0]


