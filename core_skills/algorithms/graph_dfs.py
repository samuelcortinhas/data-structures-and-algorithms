seen = set()


def dfs_recursive(node):
    # Time O(V+E), Memory O(V+E)
    if node not in seen:
        seen.add(node)
        print(node)
        for n in node.neighbours:
            dfs_recursive(n)


seen = set()
stack = []  # add source


def dfs_iterative(stack):
    # Time O(V+E), Memory O(V+E)
    while stack:
        node = stack.pop()
        print(node)
        for n in node.neighbours:
            if n not in seen:
                seen.add(n)
                stack.append(n)
