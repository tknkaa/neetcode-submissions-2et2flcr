class Solution:
    def isPalindrome(self, s: str) -> bool:
        original = [x for x in s.lower() if x.isalnum()]
        i = 0
        while i < (len(original) // 2):
            if original[i] != original[len(original) - i - 1]:
                return False
            i += 1
        return True
        