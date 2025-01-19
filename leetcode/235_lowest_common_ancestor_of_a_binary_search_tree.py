# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # Time O(h), Memory O(1)
        curr = root
        while curr:
            if curr.val > max(p.val, q.val):
                curr = curr.left
            elif curr.val < min(p.val, q.val):
                curr = curr.right
            else:
                return curr


# class Solution:
#     def dfs(self, root, p_val, q_val):
#         # assume p_val < q_val
#         if not root:
#             return False

#         if root.val > q_val:
#             return self.dfs(root.left, p_val, q_val)
#         elif root.val < p_val:
#             return self.dfs(root.right, p_val, q_val)
#         else:
#             return root

#     def lowestCommonAncestor(
#         self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
#     ) -> "TreeNode":
#         # Time O(h), Memory O(h)
#         if p.val < q.val:
#             return self.dfs(root, p.val, q.val)
#         else:
#             return self.dfs(root, q.val, p.val)
