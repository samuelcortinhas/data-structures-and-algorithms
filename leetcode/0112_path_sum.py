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

            currSum = pathSum + node.val
            if not node.left and not node.right:
                return currSum == targetSum

            return dfs(node.left, currSum, targetSum) or dfs(
                node.right, currSum, targetSum
            )

        return dfs(root, 0, targetSum)
