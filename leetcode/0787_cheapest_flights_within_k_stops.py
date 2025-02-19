from collections import defaultdict, deque
from typing import List


class Solution:
    # Time O(k*n), Memory O(n^2)
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        # k+1 iterations of bfs from src without visit set
        adj_list = defaultdict(list)
        for u, v, p in flights:
            adj_list[u].append((v, p))  # (node, price)

        min_prices = {}
        queue = deque()
        queue.append((src, 0))  # (node, price)
        for _ in range(k + 2):
            for _ in range(len(queue)):
                node, price = queue.popleft()

                if node not in min_prices or price < min_prices[node]:
                    min_prices[node] = price
                else:
                    continue

                for neigh, p in adj_list[node]:
                    queue.append((neigh, price + p))

        return min_prices.get(dst, -1)
