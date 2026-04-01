from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        tmp = ""
        for l in range(0, len(s)):
            for r in range(l, len(s)):
                part_s = s[l:(r + 1)]
                if include(part_s, t):
                    if tmp == "" or len(tmp) > len(part_s):
                        tmp = part_s
        return tmp

def include(part_s: str, t: str) -> bool:
    s_counter = Counter(part_s)
    t_counter = Counter(t)
    for k in t_counter.keys():
        if t_counter[k] > s_counter[k]:
            return False
    return True