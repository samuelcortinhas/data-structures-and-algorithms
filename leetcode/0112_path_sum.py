from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Time O(n), Memory O(h)
        def dfs(node, pathSum, targetSum):
            if not node:
                return False

            if not node.left and not node.right:
                if pathSum + node.val == targetSum:
                    return True
                else:
                    return False

            if dfs(node.left, pathSum + node.val, targetSum):
                return True
            if dfs(node.right, pathSum + node.val, targetSum):
                return True
            return False

        return dfs(root, 0, targetSum)
