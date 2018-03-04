"""
https://leetcode.com/problems/diameter-of-binary-tree
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def height(node):
            if not node:
                return -1
            lh = height(node.left) + 1
            rh = height(node.right) + 1
            if lh + rh > self.res:
                self.res = lh + rh
            return max(lh, rh)

        height(root)
        return self.res


