def bellman_ford(adj_list, src):
    # Step 1: Initialise distances
    distances = {v: float("inf") for v in adj_list}
    distances[src] = 0

    # Step 2: Relax edges |V| - 1 times
    for _ in range(len(adj_list) - 1):
        for u in adj_list:
            for v, weight in adj_list[u]:
                if (
                    distances[u] != float("inf")
                    and distances[u] + weight < distances[v]
                ):
                    distances[v] = distances[u] + weight

    # Step 3: Check for negative weight cycles
    for u in adj_list:
        for v, weight in adj_list[u]:
            if distances[u] != float("inf") and distances[u] + weight < distances[v]:
                raise ValueError("Graph contains negative weight cycle")

    return distances


# Example
adj_list = {
    "A": [("B", -1), ("C", 4)],
    "B": [("C", 3), ("D", 2), ("E", 2)],
    "C": [],
    "D": [("B", 1), ("C", 5)],
    "E": [("D", -3)],
}

shortest_distances = bellman_ford(adj_list, "A")
print(shortest_distances)
