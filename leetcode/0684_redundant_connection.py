from typing import List


class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}
        for i in range(1, n + 1):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, node):
        p = self.par[node]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, node1, node2):
        p1 = self.find(node1)
        p2 = self.find(node2)
        if p1 == p2:  # in the same set
            return False
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        elif self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Time O(n), Memory O(n)
        uf = UnionFind(len(edges))
        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]
