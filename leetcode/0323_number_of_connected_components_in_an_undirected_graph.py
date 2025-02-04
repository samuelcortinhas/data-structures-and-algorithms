from typing import List


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.height = [0] * n

    def find(self, p):
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, node1, node2):
        p1, p2 = self.find(node1), self.find(node2)
        if self.height[p1] > self.height[p2]:
            self.par[p2] = p1
        elif self.height[p1] < self.height[p2]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.height[p1] += 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Time O(n), Memory O(n)
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u, v)

        reps = set()
        for i in range(n):
            reps.add(uf.find(i))
        return len(reps)
