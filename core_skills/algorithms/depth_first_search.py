class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root):
    if not root:
        return
    dfs(root.left)
    print(root.val)
    dfs(root.right)


root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(9)
root.left.left = TreeNode(2)

dfs(root)  # 2, 7, 1, 9
