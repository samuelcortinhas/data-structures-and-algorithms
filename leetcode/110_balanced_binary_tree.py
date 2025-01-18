from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = True

    def dfs(self, node):
        # returns height of node
        if not node:
            return 0

        lh = self.dfs(node.left)
        rh = self.dfs(node.right)

        if abs(lh - rh) > 1:
            self.res = False

        return 1 + max(lh, rh)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Time O(n), Memory O(h)
        self.dfs(root)
        return self.res
