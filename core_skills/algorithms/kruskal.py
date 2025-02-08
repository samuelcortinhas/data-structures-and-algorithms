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


def kruskals(edges, n_nodes):
    # Time O(E log V), Memory O(E)
    sorted_edges = sorted(edges, key=lambda x: x[2])  # (start node, end node, weight)
    uf = UnionFind(n_nodes)
    mst = []
    for u, v, _ in sorted_edges:
        if uf.union(u, v):
            mst.append([u, v])
            if len(mst) == n_nodes - 1:
                return mst


edges = [
    (0, 1, 10),
    (0, 2, 3),
    (2, 1, 4),
    (1, 3, 1),
    (2, 3, 4),
    (2, 4, 4),
    (3, 4, 2),
]

print(kruskals(edges, 5))
