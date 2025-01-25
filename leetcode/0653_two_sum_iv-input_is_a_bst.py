from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # Time O(n), Memory O(n)
        seen = set()

        def dfs(node):
            if not node or node.val in seen:
                return False

            target = k - node.val
            if target in seen:
                return True

            seen.add(node.val)
            return dfs(node.left) or dfs(node.right)

        return dfs(root)
