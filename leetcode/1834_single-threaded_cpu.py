import heapq
from typing import List


class Solution:
    # 2 heap solution
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Time O(n log n), Memory O(n)
        curr_time = 0
        heap = [(t, d, i) for i, (t, d) in enumerate(tasks)]
        heapq.heapify(heap)
        res = []
        batch = []
        while heap or batch:
            if not batch:
                curr_time = max(curr_time, heap[0][0] if heap else 0)
            while heap and heap[0][0] <= curr_time:
                nxt = heapq.heappop(heap)
                heapq.heappush(batch, (nxt[1], nxt[2]))

            d, i = heapq.heappop(batch)
            curr_time += d
            res.append(i)
        return res

    # # a little better
    # def getOrder(self, tasks: List[List[int]]) -> List[int]:
    #     # Time O(n^2), Memory O(n)
    #     curr_time = 0
    #     heap = [(t, d, i) for i, (t, d) in enumerate(tasks)]
    #     heapq.heapify(heap)
    #     res = []
    #     batch = []
    #     while heap or batch:
    #         if not batch:
    #             curr_time = max(curr_time, heap[0][0] if heap else 0)
    #         while heap and heap[0][0] <= curr_time:
    #             batch.append(heapq.heappop(heap))

    #         shortest = float("inf")
    #         index = float("inf")
    #         del_k = None
    #         for k, b in enumerate(batch):
    #             if b[1] < shortest or (b[1] == shortest and b[2] < index):
    #                 shortest = b[1]
    #                 index = b[2]
    #                 del_k = k

    #         curr_time += shortest
    #         batch.pop(del_k)
    #         res.append(index)
    #     return res

    # # initial attempt - too slow
    # def getOrder(self, tasks: List[List[int]]) -> List[int]:
    #     # Time O((n log n)^2), Memory O(n)
    #     curr_time = 0
    #     heap = [(t, d, i) for i, (t, d) in enumerate(tasks)]
    #     heapq.heapify(heap)
    #     res = []
    #     while heap:
    #         curr_time = max(curr_time, heap[0][0])
    #         batch = []
    #         while heap and heap[0][0] <= curr_time:
    #             batch.append(heapq.heappop(heap))

    #         j = float("inf")
    #         shortest = float("inf")
    #         item = None
    #         for b in batch:
    #             if b[1] < shortest or (b[1] == shortest and b[2] < j):
    #                 shortest = b[1]
    #                 item = b
    #                 j = b[2]

    #         res.append(item[2])
    #         curr_time += item[1]
    #         for b in batch:
    #             if b != item:
    #                 heapq.heappush(heap, b)
    #     return res
