class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == "(":
                stack.append("(")
            elif ch == "{":
                stack.append("{")
            elif ch == "[":
                stack.append("[")
            elif ch == ")" and len(stack) > 0:
                if stack[len(stack) - 1] == "(":
                    stack = stack[:len(stack) - 1]
                else:
                    return False
            elif ch == "}" and len(stack) > 0:
                if stack[len(stack) - 1] == "{":
                    stack = stack[:len(stack) - 1]
                else:
                    return False
            elif ch == "]" and len(stack) > 0:
                if stack[len(stack) - 1] == "[":
                    stack = stack[:len(stack) - 1]
                else:
                    return False
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False


        