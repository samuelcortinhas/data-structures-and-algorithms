class UnionFind:
    def __init__(self, n):
        # Memory O(n)
        self.par = [i for i in range(n)]
        self.height = [0] * n

    def find(self, p):
        # Time O(a(n)) where a(.) is the inverse ackermann function (effectively constant)
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]  # path compression
            p = self.par[p]
        return p

    def union(self, node1, node2):
        # Time O(a(n)) where a(.) is the inverse ackermann function (effectively constant)
        p1, p2 = self.find(node1), self.find(node2)
        if p1 == p2:  # already in same set
            return False

        # union by height
        if self.height[p1] < self.height[p2]:
            self.par[p1] = p2
        elif self.height[p1] > self.height[p2]:
            self.par[p2] = p1
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True


class UnionFindSimple:
    def __init__(self, n):
        # Memory O(n)
        self.par = [i for i in range(n)]

    def find(self, p):
        # Time O(log n)
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, node1, node2):
        # Time O(log n)
        p1, p2 = self.find(node1), self.find(node2)
        self.par[p2] = p1
