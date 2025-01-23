from collections import deque

seen = set()
queue = deque()  # add source

while queue:
    node = queue.popleft()
    print(node)
    for n in node.neighbours:
        if n not in seen:
            seen.add(n)
            queue.append(n)
