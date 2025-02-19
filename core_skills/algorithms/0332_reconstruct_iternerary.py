from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Time O(E log V), Memory O(V+E)
        adj_list = defaultdict(list)
        for u, v in tickets:
            adj_list[u].append(v)

        for v in adj_list.values():
            v.sort(reverse=True)

        stack = ["JFK"]
        res = []
        while stack:
            while adj_list[stack[-1]]:
                stack.append(adj_list[stack[-1]].pop())
            else:
                res.append(stack.pop())
        return res[::-1]
