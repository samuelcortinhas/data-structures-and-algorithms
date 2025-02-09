import heapq
from collections import Counter, deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], buffer: int) -> int:
        # Time O(n*m), Memory O(26)
        counter = Counter(tasks)
        heap = [(-v, k) for k, v in counter.items()]
        heapq.heapify(heap)
        queue = deque()
        i = 0
        while heap or queue:
            if heap:
                freq, letter = heapq.heappop(heap)
                if freq < -1:
                    queue.append((i + buffer, freq + 1, letter))

            if queue and queue[0][0] == i:
                _, f, l = queue.popleft()
                heapq.heappush(heap, (f, l))
            i += 1
        return i
