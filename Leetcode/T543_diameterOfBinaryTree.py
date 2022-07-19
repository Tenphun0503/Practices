"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.diameter = None

    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        self.dfs(root)
        return self.diameter

    def dfs(self, node):
        if node == None:
            return 0
        left_height = self.dfs(node.left)
        right_height = self.dfs(node.right)
        self.diameter = max(self.diameter, left_height + right_height)
        return max(left_height, right_height) + 1


root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
s = Solution()
print(s.diameterOfBinaryTree(root))