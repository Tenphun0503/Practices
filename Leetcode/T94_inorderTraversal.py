"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traversal(self, node, res):
        if node == None:
            return
        self.traversal(node.left, res)
        res.append(node.val)
        self.traversal(node.right, res)

    def inorderTraversal(self, root):
        res = []
        self.traversal(root, res)
        return res


def preorder(root):
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []


def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []


def postorder(root):
    return postorder(root.left) + postorder(root.right) + [root.val] if root else []


s = Solution()
root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(s.inorderTraversal(root))
