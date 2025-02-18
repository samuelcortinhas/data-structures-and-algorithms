from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time O(n), Memory O(h)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # post order dfs
        # at each node compute max path with and without splitting
        # update result with splitting and return sum without splitting
        res = float("-inf")

        def dfs(node):
            nonlocal res
            if not node:
                return 0

            l, r = dfs(node.left), dfs(node.right)
            res = max([res, l + r + node.val, node.val + r, node.val + l, node.val])
            return max(node.val, node.val + max(l, r))

        dfs(root)
        return res
