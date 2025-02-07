import heapq
from collections import defaultdict


def dijkstras(edges, source):
    # Time O(E log V), Memory O(V)
    adj_list = defaultdict(list)
    for s, d, w in edges:  # (source, destination, weight)
        adj_list[s].append((d, w))

    shortest = {}
    heap = [(0, source)]  # (distance, node)
    while heap:
        dist, node = heapq.heappop(heap)
        if node in shortest:
            continue
        shortest[node] = dist

        for dest, weight in adj_list[node]:
            if dest not in shortest:
                heapq.heappush(heap, (dist + weight, dest))
    return shortest


edges = [
    ("A", "B", 10),
    ("A", "C", 3),
    ("C", "B", 4),
    ("B", "D", 2),
    ("C", "D", 8),
    ("C", "E", 2),
    ("D", "E", 5),
]

print(dijkstras(edges, "A"))
