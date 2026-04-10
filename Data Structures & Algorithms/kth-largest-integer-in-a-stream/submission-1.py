import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = sorted(nums, reverse = True)[:k]
        if len(self.heap) < k:
            self.heap.extend([float('-inf')] * (k - len(self.heap)))
        self.k = k
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        heapq.heappop(self.heap)
        return self.heap[0]
        
