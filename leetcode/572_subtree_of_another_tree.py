from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):
        # Time O(n), Memory O(h)
        if not p and not q:
            return True

        if not p or not q:
            return False

        l = self.isSameTree(p.left, q.left)
        r = self.isSameTree(p.right, q.right)

        if l and r and p.val == q.val:
            return True

        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Time O(n*m), Memory O(h) where n = #nodes in root and m = #nodes in subroot
        if not root and not subRoot:
            return True

        if not root:
            return False
        elif not subRoot:
            return True

        l = self.isSubtree(root.left, subRoot)
        r = self.isSubtree(root.right, subRoot)

        if root.val == subRoot.val:
            return self.isSameTree(root, subRoot) or l or r
        else:
            return l or r
