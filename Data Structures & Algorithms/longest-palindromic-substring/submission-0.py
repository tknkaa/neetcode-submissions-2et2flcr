class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        res = 0
        # odd
        for i in range(len(s)):
            tmpLen = 1
            l = i - 1
            r = i + 1
            while 0 <= l and r < len(s):
                if s[l] == s[r]:
                    tmpLen += 2
                    l -= 1
                    r += 1
                else:
                    break
            if tmpLen > resLen:
                resLen = tmpLen
                res = l + 1
        # even
        for i in range(len(s)):
            tmpLen = 0
            l = i
            r = i + 1
            while 0 <= l and r < len(s):
                if s[l] == s[r]:
                    tmpLen += 2
                    l -= 1
                    r += 1
                else:
                    break
            if tmpLen > resLen:
                resLen = tmpLen
                res = l + 1
        return s[res:(res + resLen)]
        