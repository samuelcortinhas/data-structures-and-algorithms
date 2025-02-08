from typing import List


class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbours = []


def topological_sort(nodes: List[GraphNode]):
    n = len(nodes)
    visit = set()
    res = []

    def dfs(node):
        if node not in visit:
            visit.add(node)
            for neigh in node.neighbours:
                dfs(neigh)
            res.append(node.val)

    for node in nodes:
        dfs(node)
        if len(visit) == n:
            break

    return res[::-1]


A = GraphNode(2)
B = GraphNode(7)
C = GraphNode(4)
D = GraphNode(1)
E = GraphNode(10)
A.neighbours = [B, E]
B.neighbours = [C]
C.neighbours = [D]
D.neighbours = [E]

print(topological_sort([A, B, C, D, E]))
