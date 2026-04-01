from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        tmp = ""
        l = 0
        r = 0
        t_counter = Counter(t)
        window = defaultdict(int)
        window[s[l]] = 1
        while r < len(s):
            part_of_s = s[l:(r + 1)]
            if include(window, t_counter):
                print(part_of_s)
                if tmp == "" or len(tmp) > len(part_of_s):
                    tmp = part_of_s
                window[s[l]] -= 1
                l += 1
            else:
                if r + 1 < len(s):
                    window[s[r + 1]] += 1
                r += 1
        return tmp



def include(window: Dict[str, int], t_counter: Dict[str, int]) -> bool:
    for k in t_counter.keys():
        if t_counter[k] > window.get(k, 0):
            return False
    return True