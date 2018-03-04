# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode

        if p, q are the children of root, then this func returns root.
        if one of (p, q) is one of the children of root then this func returns
        the matched children p or q.
        if none of (p, q) is the children of root, then this func returns none.
        """
        if root is None:
            return None
        if root == p or root == q:
            return root

        left, right = (self.lowestCommonAncestor(kid, p, q)
                       for kid in (root.left, root.right))

        return root if left and right else left or right
