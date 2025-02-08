from collections import defaultdict
from typing import List


class Solution:
    # Topological sort with cycle detection
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Time O(V+E), Memory O(V+E)
        adj_list = defaultdict(list)
        for a, b in prerequisites:
            adj_list[a].append(b)

        visit = set()
        path = set()  # cycle detection
        top_order = []
        cycle = False

        def dfs(node):
            nonlocal cycle
            if node in path:
                cycle = True
            if node not in visit:
                visit.add(node)
                path.add(node)
                for neigh in adj_list[node]:
                    dfs(neigh)
                top_order.append(node)
                path.remove(node)

        for i in range(numCourses):
            dfs(i)
        if cycle:
            return []
        return top_order
