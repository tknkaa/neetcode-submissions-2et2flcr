import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            print(stones)
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x == y:
                continue
            else:
                heapq.heappush(stones, - y + x)
        return -stones[0] if len(stones) > 0 else 0