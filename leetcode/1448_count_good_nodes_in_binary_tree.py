# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time O(n), Memory O(h)
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, mx):
            # recursive pre-order dfs
            if not root:
                return 0

            res = 1 if root.val >= mx else 0
            mx = max(root.val, mx)
            res += dfs(root.left, mx)
            res += dfs(root.right, mx)
            return res

        return dfs(root, root.val)


# class Solution:
#     # Time O(n), Memory O(h)
#     def goodNodes(self, root: TreeNode) -> int:
#         # iterative dfs via 2 stacks
#         # node good if top of stack is max of stack
#         good_nodes = 0
#         stack_nodes = [root]
#         stack_vals = [root.val]

#         while stack_nodes:
#             node = stack_nodes[-1]

#             if node.left:
#                 stack_nodes.append(node.left)
#                 stack_vals.append(node.left.val)
#                 node.left = None
#                 continue

#             if node.right:
#                 stack_nodes.append(node.right)
#                 stack_vals.append(node.right.val)
#                 node.right = None
#                 continue

#             if node.val == max(stack_vals):
#                 good_nodes += 1

#             stack_nodes.pop()
#             stack_vals.pop()

#         return good_nodes
