class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        max_len = 0
        while r < len(s):
            counter = Counter(s[l:(r + 1)])
            most_common = counter.most_common()[0][0]
            replacements = (r - l + 1) - counter[most_common]
            while replacements > k:
                l += 1
                counter = Counter(s[l:(r + 1)])
                most_common = counter.most_common()[0][0]
                replacements = (r - l + 1) - counter[most_common]
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len
            