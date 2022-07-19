"""
A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isUnivalTree(tree):
    if not tree:
        return True

    if tree.right:
        if tree.val != tree.right.val:
            return False

    if tree.left:
        if tree.val != tree.left.val:
            return False

    return isUnivalTree(tree.right) and isUnivalTree(tree.left)


root = TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(1, None, TreeNode(1)))
print(isUnivalTree(root))
