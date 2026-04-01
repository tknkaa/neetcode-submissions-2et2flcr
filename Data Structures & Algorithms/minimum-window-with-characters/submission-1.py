from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        tmp = ""
        l = 0
        r = 0
        while r < len(s):
            part_of_s = s[l:(r + 1)]
            if include(part_of_s, t):
                print(part_of_s)
                if tmp == "" or len(tmp) > len(part_of_s):
                    tmp = part_of_s
                l += 1
            else:
                r += 1
        return tmp



def include(part_of_s: str, t: str) -> bool:
    s_counter = Counter(part_of_s)
    t_counter = Counter(t)
    for k in t_counter.keys():
        if t_counter[k] > s_counter[k]:
            return False
    return True