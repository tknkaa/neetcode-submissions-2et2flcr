from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        count = 0
        while r < len(s):
            counter = Counter(s[l:(r + 1)])
            if counter[s[r]] > 1:
                while s[l] != s[r]:
                    l += 1
                l += 1
            if count < len(s[l:(r + 1)]):
                count = len(s[l:(r + 1)])
            r += 1
        return count