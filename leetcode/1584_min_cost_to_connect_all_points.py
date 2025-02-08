import heapq
from collections import defaultdict
from typing import List


class Solution:
    # Prim's Algorithm
    @staticmethod
    def manhattan(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Time O(n^2 log n), Memory O(n^2)
        adj_list = defaultdict(list)
        n = len(points)
        if n <= 1:
            return 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p, q = points[i], points[j]
                adj_list[tuple(p)].append(tuple(q))
                adj_list[tuple(q)].append(tuple(p))

        start = tuple(points[0])
        heap = []
        for point in adj_list[start]:
            heapq.heappush(heap, (self.manhattan(start, point), start, point))
        seen = set([start])
        cost = 0
        while heap:
            dist, start, dest = heapq.heappop(heap)
            if dest in seen:
                continue
            seen.add(dest)
            cost += dist

            if len(seen) == n:
                return cost

            for neigh in adj_list[dest]:
                if neigh not in seen:
                    heapq.heappush(heap, (self.manhattan(dest, neigh), dest, neigh))


class Solution:
    # Kruskal's algorithm
    @staticmethod
    def manhattan(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Time O(n^2 log n), Memory O(n^2)
        n = len(points)
        if n <= 1:
            return 0
        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p, q = tuple(points[i]), tuple(points[j])
                edges.append((p, q, self.manhattan(p, q)))

        sorted_edges = sorted(edges, key=lambda x: x[2])
        points_map = {tuple(p): i for i, p in enumerate(points)}
        uf = UnionFind(n)
        cost = 0
        mst_size = 0
        for u, v, w in sorted_edges:
            if uf.union(points_map[u], points_map[v]):
                cost += w
                mst_size += 1
                if mst_size == n - 1:
                    return cost


class UnionFind:
    def __init__(self, n_nodes):
        self.par = [i for i in range(n_nodes)]
        self.height = [0 for _ in range(n_nodes)]

    def find(self, p):
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]  # path compression
            p = self.par[p]
        return p

    def union(self, node1, node2):
        p1, p2 = self.find(node1), self.find(node2)
        if p1 == p2:
            return False

        # union by height
        if self.height[p1] > self.height[p2]:
            self.par[p2] = p1
        elif self.height[p1] < self.height[p2]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.height[p1] += 1
        return True
