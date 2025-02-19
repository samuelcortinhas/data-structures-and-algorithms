# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    # Both methods are: Time O(n), Memory O(n)
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # pre-order traversal with null values
        res = []

        def dfs(node):
            if not node:
                res.append("null")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return "#".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = data.split("#")
        if not vals[0]:
            return None

        i = 0

        def dfs(vals):
            nonlocal i
            if vals[i] == "null":
                i += 1
                return None
            node = TreeNode(int(vals[i]))
            i += 1
            node.left = dfs(vals)
            node.right = dfs(vals)
            return node

        return dfs(vals)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
