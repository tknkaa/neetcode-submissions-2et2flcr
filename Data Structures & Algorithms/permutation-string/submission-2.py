from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        target = defaultdict(int)
        for s in s1:
            target[s] += 1
        print("target", target)
        count = defaultdict(int)
        i = 0
        while i < len(s1):
            count[s2[i]] += 1
            i += 1
        i = 0
        while i < len(s2) - len(s1):
            print(count)
            if same_dict(target, count):
                return True
            count[s2[i]] -= 1
            count[s2[i + len(s1)]] += 1
            i += 1
        return same_dict(target, count)


def same_dict(d1: Dict[str, int], d2: Dict[str, int]) -> bool:
    for k in d1.keys():
        if d1[k] != d2[k]:
            return False
    return True