from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Time O(k), Memory O(h)
        counter = 0
        stack = [root]
        while stack:
            node = stack[-1]

            if node.left:
                stack.append(node.left)
                node.left = None
                continue

            counter += 1
            stack.pop()
            if counter == k:
                return node.val

            if node.right:
                stack.append(node.right)


# class Solution:
#     def __init__(self):
#         self.counter = 0
#         self.res = None

#     def dfs(self, root, k):
#         # in order dfs
#         if not root or self.counter == k:
#             return

#         self.dfs(root.left, k)
#         self.counter += 1
#         if self.counter == k:
#             self.res = root.val
#         self.dfs(root.right, k)

#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         # Time O(n), Memory O(h)
#         self.dfs(root, k)
#         return self.res
