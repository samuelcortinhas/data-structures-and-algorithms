from collections import defaultdict
from typing import List


class Solution:
    # DFS for every query - too slow
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        # Time O(V*Q), Memory O(V+E) where Q=len(queries)
        adj_list = defaultdict(list)
        for a, b in prerequisites:
            adj_list[a].append(b)

        def dfs(node, target, path):
            if node in path:
                return False

            if node == target:
                return True

            path.add(node)
            for neigh in adj_list[node]:
                if dfs(neigh, target, path):
                    return True
            path.remove(node)
            return False

        return [dfs(u, v, set()) for u, v in queries]
