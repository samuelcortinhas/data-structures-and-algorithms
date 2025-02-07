import heapq
from collections import defaultdict


def prims(edges):
    # Time O(E log V), Memory O(V)
    adj_list = defaultdict(list)
    for u, v, w in edges:  # start node, end node, weight
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))

    start = edges[0][0]
    visited = set([start])
    heap = []
    for start_dest, start_weight in adj_list[start]:
        heapq.heappush(heap, (start_weight, start, start_dest))
    res = []
    total_weight = 0
    while heap:
        weight, start_node, dest_node = heapq.heappop(heap)
        if dest_node in visited:
            continue
        visited.add(dest_node)
        res.append([start_node, dest_node])
        total_weight += weight

        for neigh, w in adj_list[dest_node]:
            if neigh not in visited:
                heapq.heappush(heap, (w, dest_node, neigh))

    return res, total_weight


edges = [
    ("A", "B", 10),
    ("A", "C", 3),
    ("C", "B", 4),
    ("B", "D", 1),
    ("C", "D", 4),
    ("C", "E", 4),
    ("D", "E", 2),
]

print(prims(edges))
