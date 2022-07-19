"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        pass

    def traversal(self, list, node):
        if not node:
            list.append('null')
        else:
            list.append(node.val)
            self.traversal(list, node.left)
            self.traversal(list, node.right)

    def isSameTree(self, p, q):
        list_p, list_q = [], []
        self.traversal(list_p, p)
        self.traversal(list_q, q)
        if list_p == list_q:
            return True
        else:
            return False


def solution2(p, q):
    if p and q:
        return p.val == q.val and solution2(p.left, q.left) and solution2(p.right, q.right)
    return p is q

s = Solution()
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))
print(s.isSameTree(p, q))
print(solution2(p, q))