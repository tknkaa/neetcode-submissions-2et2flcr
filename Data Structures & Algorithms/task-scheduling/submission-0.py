from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        time = 0
        freq_heap: List[int] = list(map(lambda x: -counter[x], counter))
        heapq.heapify(freq_heap)
        cooldown_queue = deque()
        while len(freq_heap) > 0 or len(cooldown_queue) > 0:
            if len(cooldown_queue) > 0 and cooldown_queue[0][0] <= time:
                available_task = cooldown_queue.popleft()
                heapq.heappush(freq_heap, -available_task[1])
            if len(freq_heap) == 0 and len(cooldown_queue) > 0:
                time = cooldown_queue[0][0]
            else:
                new_task_freq = -heapq.heappop(freq_heap)
                time += 1
                if new_task_freq - 1 > 0:
                    cooldown_queue.append((time + n, new_task_freq-1))
        return time