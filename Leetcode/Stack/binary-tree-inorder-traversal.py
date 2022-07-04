from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: Optional[TreeNode]):
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []


if __name__ == "__main__":
    tree = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    print(inorder_traversal(tree))
