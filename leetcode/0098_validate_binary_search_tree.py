from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.prev = -float("inf")
        self.res = True

    def dfs(self, root):
        if not root:
            return

        self.dfs(root.left)
        if root.val > self.prev:
            self.prev = root.val
        else:
            self.res = False
        self.dfs(root.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Time O(n), Memory O(h)
        self.dfs(root)
        return self.res
