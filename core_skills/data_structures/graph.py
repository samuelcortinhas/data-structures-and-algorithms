class GraphNode:
    def __init__(self, val, neighbours=[]):
        self.val = val
        self.neighbours = neighbours


A = GraphNode(2)
B = GraphNode(7)
C = GraphNode(4)
D = GraphNode(1)

A.neighbours.append(A, B)
B.neighbours.append(B, C, D)
C.neighbours.append(D)
