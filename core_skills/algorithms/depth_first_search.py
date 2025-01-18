class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# All are Time O(n), Memory O(h)
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)


def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)


def reverseorder(root):
    if not root:
        return
    reverseorder(root.right)
    print(root.val)
    reverseorder(root.left)


root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(9)
root.left.left = TreeNode(2)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(3)

#    1
#   7  9
#  2 5
# 3

print("in order")
inorder(root)  # 3, 2, 7, 5, 1, 9
print("\npre order")
preorder(root)  # 1, 7, 2, 3, 5, 9
print("\npost order")
postorder(root)  # 3, 2, 5, 7, 9, 1
print("\nreverse order")
reverseorder(root)  # 9, 1, 5, 7, 2, 3
