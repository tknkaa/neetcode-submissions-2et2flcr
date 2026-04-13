import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == 0:
            self.min_heap.append(num)
        elif self.min_heap[0] < num:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        if len(self.max_heap) - len(self.min_heap) > 1:
            max_num = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, max_num)
        if len(self.min_heap) - len(self.max_heap) > 1:
            min_num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_num)

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return 0.5 * (-self.max_heap[0] + self.min_heap[0])
        elif len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return self.min_heap[0]
        
        