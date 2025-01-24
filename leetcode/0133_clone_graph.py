from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        # Time O(V+E), Memory O(V+E)
        if not node:
            return None

        mapping = {}

        def dfs(node):
            if node in mapping:
                return mapping[node]

            copy_node = Node(node.val)
            mapping[node] = copy_node
            for n in node.neighbors:
                copy_node.neighbors.append(dfs(n))
            return copy_node

        return dfs(node)
