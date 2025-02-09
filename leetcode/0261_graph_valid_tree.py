from collections import defaultdict
from typing import List


class Solution:
    # Detect cycles and if graph is connected using DFS
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Time O(V+E), Memory O(E)
        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        visit = set()

        def dfs(node, parent):
            if node in visit:
                return False

            visit.add(node)
            for neigh in adj_list[node]:
                if neigh != parent:
                    if not dfs(neigh, node):
                        return False
            return True

        return dfs(0, None) and len(visit) == n


# class Solution:
#     # Detect cycles and if graph is connected using UnionFind
#     def validTree(self, n: int, edges: List[List[int]]) -> bool:
#         # Time O(V+E), Memory O(V)
#         uf = UnionFind(n)

#         for a, b in edges:
#             if not uf.union(a, b):
#                 return False

#         par = uf.find(0)
#         for i in range(1, n):
#             if uf.find(i) != par:
#                 return False
#         return True


# class UnionFind:
#     def __init__(self, n_nodes):
#         # Memory O(V)
#         self.par = [i for i in range(n_nodes)]
#         self.height = [0] * n_nodes

#     def find(self, p):
#         # Time O(a(n)) where a(.) is inverse ackermann function
#         while p != self.par[p]:
#             self.par[p] = self.par[self.par[p]]  # path compression
#             p = self.par[p]
#         return p

#     def union(self, node1, node2):
#         # Time O(a(n)) where a(.) is inverse ackermann function
#         p1, p2 = self.find(node1), self.find(node2)
#         if p1 == p2:
#             return False

#         # union by height
#         if self.height[p1] > self.height[p2]:
#             self.par[p2] = p1
#         elif self.height[p1] < self.height[p2]:
#             self.par[p1] = p2
#         else:
#             self.par[p2] = p1
#             self.height[p1] += 1
#         return True
