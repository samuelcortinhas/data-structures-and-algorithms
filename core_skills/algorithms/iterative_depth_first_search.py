class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# All are Time O(n), Memory O(h)
def in_order(root):
    stack = []
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            print(curr.val)
            curr = curr.right


def pre_order(root):
    stack = []
    curr = root
    while stack or curr:
        if curr:
            print(curr.val)
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            curr = curr.right


def post_order(root):
    # two stacks
    stack = [root]
    visit = [False]
    while stack:
        curr, visited = stack.pop(), visit.pop()
        if curr:
            if visited:
                print(curr.val)
            else:
                stack.append(curr)
                visit.append(True)
                stack.append(curr.right)
                visit.append(False)
                stack.append(curr.left)
                visit.append(False)


def reverse_order(root):
    stack = []
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.right
        else:
            curr = stack.pop()
            print(curr.val)
            curr = curr.left


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
in_order(root)  # 3, 2, 7, 5, 1, 9
print("\npre order")
pre_order(root)  # 1, 7, 2, 3, 5, 9
print("\npost order")
post_order(root)  # 3, 2, 5, 7, 9, 1
print("\nreverse order")
reverse_order(root)  # 9, 1, 5, 7, 2, 3
