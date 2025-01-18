from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = 0

    # returns height of tree
    def dfs(self, curr):
        if not curr:
            return 0

        l = self.dfs(curr.left)
        r = self.dfs(curr.right)

        self.res = max(self.res, l + r)
        return 1 + max(l, r)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Time O(n), Memory O(h)
        self.dfs(root)
        return self.res
