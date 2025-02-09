from collections import defaultdict
from typing import List


class Solution:
    # Precompute prereqs for all nodes - still too slow
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        # Time O(E^2 + Q), Memory O(V+E) where Q=len(queries)
        adj_list = defaultdict(list)
        for a, b in prerequisites:
            adj_list[a].append(b)

        def dfs(node, path, course_reqs):
            if node in path:
                return

            path.add(node)
            course_reqs.add(node)
            for neigh in adj_list[node]:
                dfs(neigh, path, course_reqs)
            path.remove(node)
            return course_reqs

        all_reqs = [0] * numCourses
        for i in range(numCourses):
            all_reqs[i] = dfs(i, set(), set())

        return [v in all_reqs[u] for u, v in queries]


# class Solution:
#     # DFS for every query - too slow
#     def checkIfPrerequisite(
#         self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
#     ) -> List[bool]:
#         # Time O(E*Q), Memory O(V+E) where Q=len(queries)
#         adj_list = defaultdict(list)
#         for a, b in prerequisites:
#             adj_list[a].append(b)

#         def dfs(node, target, path):
#             if node in path:
#                 return False

#             if node == target:
#                 return True

#             path.add(node)
#             for neigh in adj_list[node]:
#                 if dfs(neigh, target, path):
#                     return True
#             path.remove(node)
#             return False

#         return [dfs(u, v, set()) for u, v in queries]
