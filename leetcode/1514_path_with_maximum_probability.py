import heapq
from collections import defaultdict
from typing import List


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        # Time O(E log V), Memory O(V)
        adj_list = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            p = succProb[i]
            adj_list[u].append((v, p))
            adj_list[v].append((u, p))

        max_probs = {}
        heap = [(-1, start_node)]  # max heap
        while heap:
            prob, node = heapq.heappop(heap)
            if node in max_probs:
                continue
            max_probs[node] = -prob

            for dest_node, edge_prob in adj_list[node]:
                if not dest_node in max_probs:
                    heapq.heappush(heap, (prob * edge_prob, dest_node))

        return max_probs.get(end_node, 0)
