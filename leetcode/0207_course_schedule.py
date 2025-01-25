from collections import defaultdict
from typing import List


class Solution:
    # Time O(V+E), Memory O(V+E)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # detect if there is a cycle in directed graph
        adjlist = defaultdict(list)
        for a, b in prerequisites:
            adjlist[a].append(b)

        visit = set()

        def dfs(node):
            if node in visit:
                return False

            if not adjlist[node]:
                return True

            visit.add(node)
            for n in adjlist[node]:
                if not dfs(n):
                    return False

            visit.remove(node)
            adjlist[node] = []
            return True

        for x in list(adjlist.keys()):
            if not dfs(x):
                return False
        return True
