from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs(root):
    # Time O(n), Memory O(n)
    queue = deque()

    if root:
        queue.append(root)

    level = 0
    while len(queue) > 0:
        print("level:", level)
        for _ in range(len(queue)):
            node = queue.popleft()
            print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1


def bfs_simple(root):
    # Time O(n), Memory O(n)
    queue = deque()

    if root:
        queue.append(root)

    while len(queue) > 0:
        node = queue.popleft()
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


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

bfs(root)  # 1, 7, 9, 2, 5, 3
bfs_simple(root)  # 1, 7, 9, 2, 5, 3
