import copy
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ng = 0
        ok = max(piles)
        while ok - ng > 1:
            mid = (ok + ng)//2
            if enough(mid, piles, h):
                ok = mid
            else:
                ng = mid
        return ok

def enough(k: int, piles: List[int], h: int) -> bool:
    time_spent = 0
    for pile in piles:
        time_spent += (pile // k)
        if (pile // k) * k < pile:
            time_spent += 1
    return time_spent <= h